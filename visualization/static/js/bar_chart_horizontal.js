//alert(window.location.href);
var baseUrl = location.protocol+'//'+location.hostname+(location.port ? ':'+location.port: '');
//alert(full);
//var url = "http://localhost:8000/api/query/2";
var url = baseUrl + "/api/query/2";
d3.json(url, function (json) {
  console.log(json)
  console.log(json.meta.unitPx)
  console.log(json.comment)
  $('#comment').text(json.comment);
  data = json.items
  unitPx = json.meta.unitPx
  $('#myGraph').attr('height', (data.length * (20 + 5)) + 'px');
  barElements = d3.select("#myGraph")
    .selectAll("rect")
    .data(data)
  barElements.enter()
    .append("rect")
    .attr("class", "bar")
    .attr("x", 60)
    .attr("y", function(d, i) { return i * 25; })
    .attr("height", "20px")
    .attr("width", function(d, i) {
      return (d.count * unitPx) + "px";
    });
  barElements.enter()
    .append("text")
    .attr("class", "barNum")
    .attr("x", 65)
    .attr("y", function(d, i) { return (i * 25) + 15; })
    .text(function(d, i) {
      return d.count;
    });
    barElements.enter()
      .append("text")
      .attr("class", "barYaxis")
      .attr("x", 0)
      .attr("y", function(d, i) { return (i * 25) + 15; })
      .text(function(d, i) {
        return d.pref;
      });

  var table = $('#list');
  table.find('#head_unit1').text(json.meta.unit1);
  table.find('#head_unit2').text(json.meta.unit2);
  table.find('#head_sample').text(json.meta.sample_caption);
  //alert(table.find('tbody'))
  var tbody = table.find('tbody')
  for(var i = 0; i < data.length; i++) {
    var tr = $('<tr>');
    tr.append('<td>' + (i + 1) + '</td>');
    tr.append('<td>' + data[i].pref + '</td>');
    tr.append('<td>' + data[i].count + '</td>');
    tr.append('<td>' + data[i].sample + '</td>');
    tbody.append(tr);
  }

});
