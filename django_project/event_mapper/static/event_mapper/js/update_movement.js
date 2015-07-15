/**
 * Created by ismailsunni on 5/13/15.
 */


var current_region;
var risk_level_colors = ['white', 'lime', 'yellow', 'red', 'black'];

function update_current(region_name, risk_level, movement_state){
    $('#current_region').text(region_name);
    $('#current_risk_level').text(risk_level);
    $('#current_movement_state').text(movement_state);
}

function add_current_region_geojson(geojson_data, risk_level_id){
    if (current_region){
        map.removeLayer(current_region);
    }

    current_region = L.geoJson(geojson_data, {
        style: function () {
            return {
                weight: 3,
                fillColor: risk_level_colors[risk_level_id - 1],
                color: 'blue',
                dashArray: '1'
            }
        }
    });
    current_region.addTo(map);
}

function add_provinces(provices){
    var province_select = $('#id_province');
    province_select.empty();
    var option = new Option("Entire Country", '0');
    province_select.append(option);
    console.log(provices);
    $.each(provices, function(index, province){
        var option = new Option(province[1], province[0]);
        province_select.append(option);
    });
    province_select.parent().parent().show();
}

function set_dropdown_color(){
    $('select[id=id_risk_level]').children().each(function (){

        $(this).attr('style', 'background-color:' + risk_level_colors[$(this).val() - 1] + ';');
    });
    var risk_level = $('#id_risk_level');
    risk_level.on('change', function() {
        risk_level.attr('style', 'background-color:' + risk_level_colors[risk_level.val() - 1] + ';');
    });
}

function set_chosen_risk_level_color(){
    var risk_level = $('#id_risk_level');
    risk_level.attr('style', 'background-color:' + risk_level_colors[risk_level.val() - 1] + ';');
}