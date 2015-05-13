/**
 * Created by ismailsunni on 5/13/15.
 */


var current_region;

function update_current(region_name, risk_level, movement_state){
    $('#current_region').text(region_name);
    $('#current_risk_level').text(risk_level);
    $('#current_movement_state').text(movement_state);
}

function add_current_region(array_polygon){
    if (current_region){
        map.removeLayer(current_region);
    }

    current_region = L.polygon(array_polygon).addTo(map);
}