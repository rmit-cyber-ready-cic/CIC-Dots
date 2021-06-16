// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["jun-20", "jul-20", "aug-20", "sept-20", "oct-20", "nov-20", "dec-20", "jan-21", "feb-21", "mar-21", "apr-21", "may-21"],
    datasets: [{
      label: "Planned",
      backgroundColor: "#46BFBD",
      borderColor: "#5AD3D1",
      data: [30,	25,	28,	20,	32,	25,	28,	26,	20,	26,	31,	15],
    },
    {
      label: "Unplanned",
      backgroundColor: "#F7464A",
      borderColor: "#FF5A5E",
      data: [3,	5,	2,	6,	1,	0,	4,	0,	4,	6,	3,	1],
    },
  ],
  },
  options: {
    scales: {
      xAxes: [{
        stacked: true,
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 12
        }
      }],
      yAxes: [{
        stacked: true,
        ticks: {
          min: 0,
          max: 40,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
