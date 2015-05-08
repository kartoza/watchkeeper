/**
 * Created by ismailsunni on 4/9/15.
 */

var map;

function show_map(bounds) {
    'use strict';
    $('#navigationbar').css('height', window.innerHeight * 0.1);
    $('#map').css('height', window.innerHeight * 0.9);
    if (bounds){
        //map = L.map('map').setView([-6.2000, 106.8167], 11);
        map = L.map('map').fitBounds(bounds);
    }else{
        map = L.map('map').setView([-6.2000, 106.8167], 11);
    }
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

}

function set_offset() {
    'use strict';
    var navbar, navbar_height, map, content, map_offset, content_offset;
    navbar = $('.navbar');
    navbar_height = navbar.height();
    map = $('#map');
    content = $('#content');

    if (map.length) {
        map_offset = map.offset();
        map.offset({top: navbar_height, left: map_offset.left});
    }
    if (content.length) {
        content_offset = content.offset();
        content.offset({top: navbar_height, left: content_offset.left});
    }
}

function toggle_side_panel() {
    'use strict';
    var map_div = $('#map'),
        side_panel = $('#side_panel'),
        show_hide_div = $('#show_hide');
    /* hide */
    if (side_panel.is(":visible")) {
        show_hide_div.removeClass('glyphicon-chevron-right');
        show_hide_div.addClass('glyphicon-chevron-left');
        side_panel.removeClass('col-lg-4');
        side_panel.hide();
        map_div.removeClass('col-lg-8');
        map_div.addClass('col-lg-12');
        map.invalidateSize();
    } else { /* show */
        show_hide_div.addClass('glyphicon-chevron-right');
        show_hide_div.removeClass('glyphicon-chevron-left');
        side_panel.addClass('col-lg-4');
        side_panel.show();
        map_div.removeClass('col-lg-12');
        map_div.addClass('col-lg-8');
        map.invalidateSize();
    }
}

function map_change_bound(){

}

