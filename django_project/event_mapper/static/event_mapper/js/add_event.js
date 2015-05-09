/**
 * Created by ismailsunni on 5/9/15.
 */

var new_event_marker;

function update_incident_advisory(){
    $('input:radio[name=category]').change(function() {
        var killed_input = $('#id_killed');
        var killed_field = $("label[for=id_killed]")
        var injured_input = $('#id_injured');
        var injured_field = $("label[for=id_injured]")
        var detained_input = $('#id_detained');
        var detained_field = $("label[for=id_detained]")
        if (this.value == '1') {
            // Incident, show all
            killed_input.show();
            killed_field.show();
            injured_input.show();
            injured_field.show();
            detained_input.show();
            detained_field.show();
        }
        else if (this.value == '2'){
            // Advisory, hide all
            killed_input.hide();
            killed_field.hide();
            injured_input.hide();
            injured_field.hide();
            detained_input.hide();
            detained_field.hide();
        }
    });
}

function place_name_autocomplete(){
    $("#id_place_name").autocomplete({
        source: function( request, response ) {
            $.ajax({
                url: "http://gd.geobytes.com/AutoCompleteCity",
                dataType: "jsonp",
                data: {
                    q: request.term
                },
                success: function( data ) {
                    response( data );
                }
            });
        },
        minLength: 3,
        select: function( event, ui ) {
            var geocoder =  new google.maps.Geocoder();
            geocoder.geocode( { 'address': $('#id_place_name').val()},
                function(results, status) {
                    if (status == google.maps.GeocoderStatus.OK) {
                        var lat = results[0].geometry.location.lat();
                        var lng = results[0].geometry.location.lng();

                        set_latitude_form(lat);
                        set_longitude_form(lng);
                        var context = {
                            'lat': lat, 'lng': lng
                        };
                        update_new_event_marker(lat, lng);
                        show_map(context);
                    } else {
                        alert("Something got wrong with location " +
                        "autocomplete." + status);
                    }
                });
        },
        open: function() {
            $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
        },
        close: function() {
            $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
        }
    });
}


function update_new_event_marker(lat, lng){
    if (new_event_marker){
        map.removeLayer(new_event_marker);
    }
    new_event_marker = new L.marker([lat, lng], {id:'uni', draggable:'true'});
    set_latitude_form(lat);
    set_longitude_form(lng);

    new_event_marker.on('dragend', function(event){
        var new_event_marker = event.target;
        var position = new_event_marker.getLatLng();
        set_long_lat_form(position);
        new_event_marker.setLatLng(position,{id:'uni', draggable:'true'});
    });
    new_event_marker.addTo(map);
}

function add_marker_on_click(e){
    update_new_event_marker(e.latlng.lat, e.latlng.lng);
}

function set_longitude_form(longitude){
    $('#id_longitude').val(longitude);
}

function set_latitude_form(latitude){
    $('#id_latitude').val(latitude);
}

function set_long_lat_form(latlng){
    set_latitude_form(latlng.lat);
    set_longitude_form(latlng.lng);
}