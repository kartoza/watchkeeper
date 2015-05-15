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
    iconUrl: icon_urls[0]
});

var advisory_icon = L.icon({
    iconUrl: icon_urls[1]
});


function add_event_marker(event_context){
    // Variables
    var event_marker;
    var event_icon;
    var lat = event_context['geometry']['coordinates'][0];
    var lng = event_context['geometry']['coordinates'][1];
    var event_id = event_context['properties']['id'];
    var event_place_name = event_context['properties']['place_name'];
    var event_type = event_context['properties']['type'];
    var event_category = event_context['properties']['category'];
    // Draw event marker
    if (event_category == 1){
        event_icon = incident_icon;
    } else if (event_category == 2){
        event_icon = advisory_icon;
        event_icon = L.icon({});
    } else {
        event_icon = L.icon();
    }
    event_marker = L.marker(
        [lat, lng], {id: event_id, icon: event_icon}).addTo(map);

    // Add to markers
    markers[event_id] = event_marker;
}