import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data=pandas.read_csv("reviews.csv",parse_dates=['Timestamp'])
data['Weekday']=data['Timestamp'].dt.strftime('%A')
data['Daynumber']=data['Timestamp'].dt.strftime('%w')
weekday_avg=data.groupby(['Weekday','Daynumber']).mean()
weekday_avg=weekday_avg.sort_values('Daynumber')

chart_def= """
{
  chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: 'Aggregated Average Rating by Day of the Week'
  },
  subtitle: {
    text: 'Happiest Day'
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Weekday'
    },
    labels: {
      format: '{value}'
    },
    accessibility: {
      rangeDescription: 'Range: 0 to 80 km.'
    },
    maxPadding: 0.05,
    showLastLabel: true
  },
  yAxis: {
    title: {
      text: 'Average Rating'
    },
    labels: {
      format: '{value}'
    },
    accessibility: {
      rangeDescription: 'Range: -90°C to 20°C.'
    },
    lineWidth: 2
  },
  legend: {
    enabled: false
  },
  tooltip: {
    headerFormat: '<b>{series.name}</b><br/>',
    pointFormat: '{point.x} {point.y}'
  },
  plotOptions: {
    spline: {
      marker: {
        enable: false
      }
    }
  },
  series: [{
    name: 'Average Rating',
    data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
      [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
  }]
}
"""

def app():
    wp=jp.QuasarPage()
    h1=jp.QDiv(a=wp, text="Analysis of Course Reviews", classes= "text-h3 text-center q-pa-md")
    p1=jp.QDiv(a=wp, text="These graphs represent course review analysis.")
    hc=jp.HighCharts(a=wp, options= chart_def)
    hc.options.title.text="Average Rating by Week"

    hc.options.xAxis.categories=list(weekday_avg.index.get_level_values(0))
    hc.options.series[0].data= list(weekday_avg['Rating'])

    return wp

jp.justpy(app)