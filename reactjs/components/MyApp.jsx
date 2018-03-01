import React from "react"
import ReactDOM from 'react-dom';
import fusioncharts from 'fusioncharts';
import ReactFC from 'react-fusioncharts';
import charts from 'fusioncharts/fusioncharts.charts';

var data1 = ''
var data_321 =  [{
            label: 'Bakesdfdsfrsfield Central',
            value: '880000'
        }, {
            label: 'Gardedsfsdfn Groove harbour',
            value: '730000'
        }, {
            label: 'Los Ansdfgeles Topanga',
            value: '590000'
        }, {
            label: 'Comptosdfn-Rancho Dom',
            value: '520000'
        }, {
            label: 'Daly Cisdfty Serramonte',
            value: '330000'
        }]
var data_123 = [{
            label: 'Bakersfield Central',
            value: '880000'
        }, {
            label: 'Garden Groove harbour',
            value: '730000'
        }, {
            label: 'Los Angeles Topanga',
            value: '590000'
        }, {
            label: 'Compton-Rancho Dom',
            value: '520000'
        }, {
            label: 'Daly City Serramonte',
            value: '330000'
        }] 

var value = '';






    var myDataSource = {
        chart: {
            caption: "Harry's SuperMart",
            subCaption: 'Top 5 stores in last month by revenue',
            numberPrefix: '$',
            theme: 'ocean'
        },
        data: data1
    };

    export default class GithubRepos extends React.Component{

        getInitialState: function () {
        console.log("inited");
            return {
                filterSource: '',
                data1 : ""
            };
        },

        handleChange: function (event) {

        const target = event.target;
        var is_check = target.checked;
        var value = target.value;
        if(is_check == true){
        	fetch('http://127.0.0.1:8000/details'+'?ap='+value,{
		      method:"GET"})
		          .then(function(response) {
		              return response.json()
		          }).then(function(json) {
		              data1 = json;
		              
		              
		             
		          })
	        this.setState({
	                filterSource: 'btn-update-data'
	            });
	            
        }
      

        },
               
        render: function () {
            var revenueChartConfigs = {
                id: 'monthly-revenue-chart',
                renderAt: 'monthly-revenue-chart-container',
                type: 'column2d',
                width: 500,
                height: 400,
                dataFormat: 'json',
                dataSource: myDataSource,
                eventSource: this.state.filterSource,
                impactedBy: ['btn-update-data', 'a']
            };
             console.log(data1);
            if (this.state.filterSource == 'btn-update-data') {
            console.log(this.state.filterSource);
                revenueChartConfigs.dataSource.data = data1
            } else {
            console.log(this.state.filterSource, "123");
                revenueChartConfigs.dataSource.data = data_123;
            }

            return (
            <div className="container">
		        <div className="row">
		          <div className="col-sm-12">
		                <div>
		                    <ReactFC {...revenueChartConfigs} />
		                    <input type="radio" name="same" id='btn-update-data'
		                        onChange={this.handleChange}
		                        className='btn btn-default' value="sales"
		                       checked={this.props.checked}>{'Click me to change data'}</input>
		                       <input type="radio" name="same" id='btn-update-data'
		                        onChange={this.handleChange}
		                        className='btn btn-default' value="python"
		                       checked={this.props.checked}>{'Click me to change data'}</input>
		                       <input type="radio" name="same" id='btn-update-data'
		                        onChange={this.handleChange}
		                        className='btn btn-default' value="cool"
		                       checked={this.props.checked}>{'Click me to change data'}</input>
		                       <input type="radio" name="same" id='btn-update-data'
		                        onChange={this.handleChange}
		                        className='btn btn-default' value="best"
		                       checked={this.props.checked}>{'Click me to change data'}</input>
		                </div>
		               </div>
            	</div>
			</div>
            );
        }
    }
    


