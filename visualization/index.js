// Set bounds
let svgWidth = 600, svgHeight = 400
let margin = { top: 20, right: 20, bottom: 30, left: 50 }
let width = svgWidth - margin.left - margin.right
let height = svgHeight - margin.top - margin.bottom

// fn to Draw Line Chart 
drawLineChart = (divId, dataRows) => {

    // Append svg to draw the chart into
    let svg = d3.select(divId)
        .append('svg')
        .attr('width', svgWidth)
        .attr('height', svgHeight)

    let g = svg.append('g')
        .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')

    // Define X Axis - Dates
    let x = d3.scaleTime()
        .domain(d3.extent(dataRows, d => d.Date))
        .rangeRound([0, width])
    // Append X Axis
    g.append('g')
        .attr('transform', 'translate(0,' + height + ')')
        .call(d3.axisBottom(x))
        // X Axis text
        .append('text')
        .style("text-anchor", "end")
        .attr('transform', 'translate(' + width + ', 0)')
        .attr('fill', '#000')
        .attr('y', 0)
        .attr('dy', '-0.71em')
        .text('Timeline')

    // Define Y Axis - Prices
    let y = d3.scaleLinear()
        .domain(d3.extent(dataRows, d => d.Price))
        .rangeRound([height, 0])
    // Append Y Axis
    g.append('g')
        .call(d3.axisLeft(y))
        // Y Axis text
        .append('text')
        .attr('transform', 'rotate(-90)')
        .attr('fill', '#000')
        .attr('y', 6)
        .attr('dy', '0.71em')
        .attr('text-anchor', 'end')
        .text('Price ($ per mil. BTU)');

    // Line generator
    let line = d3.line()
        .x(d => x(d.Date))
        .y(d => y(d.Price))

    // Append path
    g.append('path')
        .datum(dataRows)
        .attr('fill', 'none')
        .attr('stroke', 'steelblue')
        .attr('stroke-linejoin', 'round')
        .attr('stroke-linecap', 'round')
        .attr('stroke-width', 1.5)
        // with d value seeded by the line generator 
        .attr('d', line);
}

csvToLineChart = (divId, csvFile, dateParseString) => {
    // Import data and draw line chart
    d3.csv(csvFile)
        .row((d) => {
            return { Date: d3.timeParse(dateParseString)(d.date), Price: +d.price }
        })
        .get((err, rows) => {
            drawLineChart(divId, rows)
        })
}
