/**
 * Created by ismailsunni on 5/13/15.
 */


var current_region;

function update_current(region_name, risk_level, movement_state){
    $('#current_region').text(region_name);
    $('#current_risk_level').text(risk_level);
    $('#current_movement_state').text(movement_state);
}

function add_current_region_geojson(geojson_data){
    if (current_region){
        map.removeLayer(current_region);
    }

    current_region = L.geoJson(geojson_data, {
        style: function () {
            return {weight: 1, color: "#000000"}
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
        console.log('here');
        province_select.append(option);
    });
    province_select.parent().parent().show();
}