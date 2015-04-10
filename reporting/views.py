from django.shortcuts import render

from django.views.generic import TemplateView, DetailView

from lms.models import ClassPlSummary

## Import django database connection
from django.db import connection

# Create your views here.

class ReportView(TemplateView):

    template_name = 'reporting/report_view.html'

    def get_context_data(self, **kwargs):

        ##JMW profit numbers
        cursor = connection.cursor()
        cursor.execute("SELECT SUM(net_profit) from lms_classplsummary WHERE start_date >= '2014-01-01' AND start_date < '2015-01-01'")
        profit_2014 = cursor.fetchall()
        jm_2014 = float(profit_2014[0][0])
        cursor.execute("SELECT SUM(net_profit) from lms_classplsummary WHERE start_date >= '2015-01-01' AND start_date < '2016-01-01'")
        profit_2015 = cursor.fetchall()
        jm_2015 = float(profit_2015[0][0])

        ## JMW Facility Expense totals
        cursor.execute("SELECT SUM(facility_expense) from lms_classplsummary WHERE start_date >= '2014-01-01' AND start_date < '2015-01-01'")
        fe_2014 = cursor.fetchall()
        facility_expense_2014 = float(fe_2014[0][0])
        cursor.execute("SELECT SUM(facility_expense) from lms_classplsummary WHERE start_date >= '2015-01-01' AND start_date < '2016-01-01'")
        fe_2015 = cursor.fetchall()
        facility_expense_2015 = float(fe_2015[0][0])

        #JM Instructor Expenses
        cursor.execute("SELECT SUM(instructor_expense) from lms_classplsummary WHERE start_date >= '2014-01-01' AND start_date < '2015-01-01'")
        instructor_2014 = cursor.fetchall()
        instructor_expense_2014 = float(instructor_2014[0][0])
        cursor.execute("SELECT SUM(instructor_expense) from lms_classplsummary WHERE start_date >= '2015-01-01' AND start_date < '2016-01-01'")
        instructor_2015 = cursor.fetchall()
        instructor_expense_2015 = float(instructor_2015[0][0])

        return {'jm_2014': jm_2014, 'jm_2015': jm_2015, 'facility_expense_2014':facility_expense_2014, 'facility_expense_2015':facility_expense_2015,
                'instructor_expense_2014': instructor_expense_2014, 'instructor_expense_2015':instructor_expense_2015}

reporting_view = ReportView.as_view()

class RosterView(TemplateView):
    template_name = 'reporting/roster_view.html'

    def get_context_data(self, **kwargs):
        cursor = connection.cursor()
        cursor.execute("select * from roster_view")
        public_classes = cursor.fetchall()
        return {'public_classes': public_classes}


class RosterByCourse(DetailView):
    model = ClassPlSummary
    template_name = 'reporting/roster_by_course.html'
    queryset = ClassPlSummary.objects.all()
    query_pk_and_slug = False

