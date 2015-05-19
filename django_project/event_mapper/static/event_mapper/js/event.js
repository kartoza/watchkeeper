/**
 * Created by ismailsunni on 5/9/15.
 */

var markers = [];

var event_layer = new L.LayerGroup();
var icon_urls = [
    'static/event_mapper/css/images/blast-blue.png',
    'static/event_mapper/css/images/blast-red.png',
    'static/event_mapper/css/images/blast-blue-selected.png',
    'static/event_mapper/css/images/blast-red-selected.png'
];
var pie_chart;

var incident_icon = L.icon({
    iconUrl: icon_urls[0],
    iconAnchor: [16, 37]
});

var advisory_icon = L.icon({
    iconUrl: icon_urls[1],
    iconAnchor: [16, 37]
});

var selected_incident_icon = L.icon({
    iconUrl: icon_urls[2],
    iconAnchor: [16, 37]
});

var selected_advisory_icon = L.icon({
    iconUrl: icon_urls[3],
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
            [lat, lng],
            {
                id: event_id,
                icon: event_icon,
                event_category: event_category,
                event_place_name: event_place_name,
                event_selected: false
            }
        ).addTo(map);
    }else{
        event_marker = L.marker(
            [lat, lng], {id: event_id}).addTo(map);
    }

    event_marker.on('click', on_click_marker);
    //event_marker.bindPopup(event_place_name);

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

function create_chart(mdata) {
    if (pie_chart){
        pie_chart.destroy();
    }
    console.log('Create chart');
    console.log(mdata);
    var container = $("#incident_type_chart").get(0).getContext("2d");
    var data = [
        {
            value: mdata['advisory'],
            color:"#C74444",
            highlight: "#FF5A5E",
            label: "Advisory"
        },
        {
            value: mdata['incident'],
            color: "#202BAD",
            highlight: "#5AD3D1",
            label: "Incident"
        }
    ];
    pie_chart = new Chart(container).Pie(data, {animateScale: true});
}

function on_click_marker(e){
    var is_selected = this.options.event_selected;
    for (var i = 0; i < markers.length; i++){
        if (markers[i]){
            set_icon(markers[i], false);
        }
    }
    if (is_selected){
        set_icon(this, false);
        show_dashboard();
    } else{
        set_icon(this, true);
        show_event_detail(this);
    }
}

function set_icon(event, selected){
    if (event.options.event_category == 1){
        if (selected){
            event.setIcon(selected_incident_icon);
        } else{
            event.setIcon(incident_icon);
        }
    } else if (event.options.event_category == 2){
        if (selected){
            event.setIcon(selected_advisory_icon);
        } else{
            event.setIcon(advisory_icon);
        }
    }
    event.options.event_selected = selected;
}

function show_event_detail(event){
    $('#event_dashboard').hide();
    $('#event_detail').show();
    console.log(event.options.event_place_name);
}

function show_dashboard(){
    $('#event_dashboard').show();
    $('#event_detail').hide();
}