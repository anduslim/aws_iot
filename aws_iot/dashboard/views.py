from __future__ import absolute_import, unicode_literals
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin
from aws_iot.users.models import User
from .models import MedicationIntake, SensorNode, DerivedIntakeReading
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import datetime, json
from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotFound


class DashboardRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("dashboard:dashboard")


class DashboardMainView(LoginRequiredMixin, TemplateView):
    '''
    A Template View to display dashboard
    '''

    template_name = 'dashboard/dashboard.html'


    def get_context_data(self, **kwargs):
        ctx = super(DashboardMainView, self).get_context_data(**kwargs)


        ctx.update({
                'overall_status': 'OK',
                'overall_message': 'All services and hosts are up and running',
                'services': {
                            'overall_status': 'OK',
                            'count': '2 running',
                            'services':
                            [
                                {'name': 'Openfire',
                                 'status': 'Running'
                                },
                                {'name': 'Kamailio',
                                 'status': 'Running'
                                }
                            ]
                    },
                'hosts': {
                         'overall_status': 'OK',
                         'count': '1 active',
                         'hosts':
                         [
                            {'name': 'app',
                             'IP': '192.168.100.1',
                             'status': 'Active'
                            }
                         ]
                    },
                'notifications': [
                         {'Date': '22 July 2015 0715HR',
                          'Loglevel': 'Info',
                          'Message': 'All services running.'
                         },
                         {'Date': '22 July 2015 0615HR',
                          'Loglevel': 'Warning',
                          'Message': 'Openfire was restarted.'
                         },
                         {'Date': '22 July 2015 0415HR',
                          'Loglevel': 'Error',
                          'Message': 'Openfire was stopped.'
                         },

                    ]
            })
        return ctx

    def dispatch(self, *args, **kwargs):
        return super(DashboardMainView, self).dispatch(*args, **kwargs)


class DashboardManageView(LoginRequiredMixin, TemplateView):
    '''
    A Template View to display manage control
    '''

    template_name = 'dashboard/manage.html'


    def get_context_data(self, **kwargs):
        ctx = super(DashboardManageView, self).get_context_data(**kwargs)


        ctx.update({
                'services': {
                            'overall_status': 'OK',
                            'count': '3 running',
                            'services':
                            [
                                {'name': 'Openfire',
                                 'host': 'AppServer',
                                 'uptime': '1 day 17:33:23',
                                 'status': 'Running'
                                },
                                {'name': 'Kamailio',
                                 'host': 'AppServer',
                                 'uptime': '07:55:49',
                                 'status': 'Running'
                                },
                                {'name': 'FreeSwitch',
                                 'host': 'ProxyServer',
                                 'uptime': '1 week 11:23:04',
                                 'status': 'Running'
                                },

                            ]
                    },
                'hosts': {
                         'overall_status': 'OK',
                         'count': '2 active',
                         'hosts':
                         [
                            {'name': 'AppServer',
                             'IP': '192.168.100.1',
                             'status': 'Active',
                             'services_running': 2,
                             'services_stopped': 0
                            },
                            {'name': 'ProxyServer',
                             'IP': '192.168.100.2',
                             'status': 'Active',
                             'services_running': 1,
                             'services_stopped': 0
                            }
                         ]
                    }
            })
        return ctx

    def dispatch(self, *args, **kwargs):
        return super(DashboardManageView, self).dispatch(*args, **kwargs)


class DashboardUserView(LoginRequiredMixin, TemplateView):
    '''
    A Template View to display user control
    '''

    template_name = 'dashboard/user.html'


    def get_context_data(self, **kwargs):
        ctx = super(DashboardUserView, self).get_context_data(**kwargs)


        ctx.update({
                'overall_status': 'OK',
                'overall_message': 'All services and hosts are up and running',
                'services': {
                            'overall_status': 'OK',
                            'count': '2 running',
                            'services':
                            [
                                {'name': 'Openfire',
                                 'status': 'Running'
                                },
                                {'name': 'Kamailio',
                                 'status': 'Running'
                                }
                            ]
                    },
                'hosts': {
                         'overall_status': 'OK',
                         'count': '1 active',
                         'hosts':
                         [
                            {'name': 'app',
                             'IP': '192.168.100.1',
                             'status': 'Active'
                            }
                         ]
                    },
                'notifications': [
                         {'Date': '22 July, 2015',
                          'Loglevel': 'Warning',
                          'Message': 'Openfire was restarted on 22 July 2015 0615HR.'
                         }
                    ]
            })
        return ctx

    def dispatch(self, *args, **kwargs):
        return super(DashboardUserView, self).dispatch(*args, **kwargs)


@csrf_exempt
def get_intake_timing_api(request, **kwargs):
    '''
    API HTTP GET call to retrieve medication intake timings
    HTTP parameters: seqno, timestamp, node_id, sensor_id, readings
    '''

    data = request.GET
    node_id = data.get('node_id', 100)

    readings = SensorNode.objects.filter(node_id=node_id)

    # should return only one reading
    # for reading in readings:
    reading = readings[0]
    
    if readings:
        payload = []
        for med_intake in reading.medication_intake_list.all():
            payload.append(med_intake.expected_intake_timing)
        print(payload)

        response_data = {}
        response_data['status'] = {'code': 200,
                                    'timestamp': datetime.datetime.now(),
                                }


        response_data['readings'] = {
                                    'node_id': node_id,
                                    'expected_timings': payload,
                                    'threshold_min': reading.timing_threshold_min,
                                    }

        return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), status=200, content_type="application/json")
    else:
        messages.add_message(request, messages.ERROR, "Error!Readings do not exist.")
        return HttpResponseNotFound(content=dict(error_code=404, error_msg="Readings do not exist."))


@csrf_exempt
def post_derived_reading_api(request, **kwargs):
    '''
    API HTTP POST call to send node readings
    HTTP parameters: seqno, timestamp, node_id, sensor_id, readings
    '''

    data = request.POST
    sensor_id = data.get('sensor_id', 100)
    is_open = data.get('is_open', None)
    if sensor_id is None or is_open is None:
        return HttpResponse(status=404)

    try:
        node = SensorNode.objects.get(node_id=sensor_id)
    except SensorNode.DoesNotExist:
        return HttpResponse(status=404)

    payload = {"sensor_id": sensor_id, "isOpen": is_open}
    reading = DerivedIntakeReading.objects.create_reading(payload)

    response_data = {}
    response_data['status'] = {'code': 200,
                                'timestamp': timestamp,
                            }

    response_data['readings'] = { 'node_id': sensor_id,
                                'is_open': is_open
                                }

    return HttpResponse(json.dumps(response_data), status=200, content_type="application/json")