/**
 * Created by ismailsunni on 5/9/15.
 */

var markers = [];

var event_layer = new L.LayerGroup();
var icon_urls = [
    'static/event_mapper/css/images/blue-blast.png',
    'static/event_mapper/css/images/red-blast.png'
];

var incident_icon = L.icon({
    iconUrl: icon_urls[0],
    iconAnchor: [16, 37]
});

var advisory_icon = L.icon({
    iconUrl: icon_urls[1],
    iconAnchor: [16, 37]
});


function add_event_marker(event_context){
    // Variables
    var event_marker;
    var event_icon;
    var lat = event_context['geometry']['coordinates'][1];
    var lng = event_context['geometry']['coordinates'][0];
    console.log('Adding to ' + [lat, lng]);
    var event_id = event_context['properties']['id'];
    var event_place_name = event_context['properties']['place_name'];
    var event_type = event_context['properties']['type'];
    var event_category = event_context['properties']['category'];
    // Draw event marker
    if (event_category == 1){
        event_icon = incident_icon;
    } else if (event_category == 2) {
        event_icon = advisory_icon;
    }
    if (event_icon) {
        event_marker = L.marker(
            [lat, lng], {id: event_id, icon: event_icon}).addTo(map);
    }else{
        event_marker = L.marker(
            [lat, lng], {id: event_id}).addTo(map);
    }

    event_marker.bindPopup('loc ' + [lng, lat, event_place_name]);

    // Add to markers
    markers[event_id] = event_marker;
}

function clear_markers(){
    for(var i  = 0; i < markers.length; i++){
        if (markers[i]){
            map.removeLayer(markers[i]);
        }
    }
    markers = [];
}

function interval_changes(radio_button){
    if (radio_button.value == 'custom'){
        enable_custom_interval(true);
    } else{
        enable_custom_interval(false);
    }
}

function enable_custom_interval(bool){
    $('#end_time_input').prop('disabled', !bool);
    $('#start_time_input').prop('disabled', !bool);

}