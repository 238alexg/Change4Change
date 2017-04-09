
var map;
//#141414

function initMap(){
	var styleArray = [
	 {
		featureType: "road",
		elementType: "labels",
		stylers: [
		  { visibility: "off" }
		]
	  }
	  ,{
		featureType: "poi",
		elementType: "all",
		stylers: [
		  { visibility: "off" }
		]
	  }
	  ,{
		featureType: "water",
		stylers: [
		  { "color": "#161616" }
		]
	  }
	  ,{
		featureType: "landscape",
		stylers: [
		  {"color": "#BBBBBB"}
		]
	  }
	  ,{
		featureType: "administrative",
		stylers: [
		  { visibility: "off" }
		]
	  },{
		featureType: "administrative.locality",
		stylers: [
		  { visibility: "on" }
		]
	  }
	];
  map = new google.maps.Map(document.getElementById('map'), {
    center: {
      lat: 44.052,
      lng: -123.086
    },
	styles: styleArray,
    zoom: 14
  });
	var trafficLayer = new google.maps.TrafficLayer();
	trafficLayer.setMap(map);
	
	marker = new google.maps.Marker({
      map: map
    });
	map.addListener('rightclick', function(e) {
        createWindow(e);
    });

    addMarkers();
}

function createWindow(e) {
    marker.setPosition(e.latLng);
    
    //set position data
    var latitude = e.latLng.lat();
    var longitude = e.latLng.lng();
    var lat = document.getElementById("lat");
    lat.setAttribute("value", latitude);
    var long = document.getElementById("long");
    long.setAttribute("value", longitude);
    console.log("Latitude: " + latitude +'\n' +"Longitude: " + longitude);
    
    infowindow = new google.maps.InfoWindow;
     var formData = document.getElementById('form');
    infowindow.setContent(formData);
    infowindow.open(map, marker);
    google.maps.event.addListener(infowindow,'closeclick',function(){
        window.location.reload();
   // then, remove the infowindows name from the array
});

}

function addMarkers() {
    var markersOld = [
        [ 44.052, -123.086, "a test"],
        [ 44.032, -123.087, "a test2"]
    ];
    /*var locations = [];
    for(i = 0; i < markersOld.length; i++)
    {
        var aLoc = {lat: markersOld[i][0], lng: markersOld[i][1]};
        locations.push(aLoc);
    }

    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location
        });
    });*/

    // Add a marker clusterer to manage the markers.
    /*var markerCluster = new MarkerClusterer(map, markers,
        {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
    */
     var infoWindow = new google.maps.InfoWindow(), marker, i;
     for( i = 0; i < markersOld.length; i++ ) {
        var position = new google.maps.LatLng(markersOld[i][0], markersOld[i][1]);
        //bounds.extend(position);
        marker = new google.maps.Marker({
            position: position,
            map: map,
        });
        
        // Allow each marker to have an info window    
        google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
                infoWindow.setContent(markersOld[i][2]);
                infoWindow.open(map, marker);
            }
        })(marker, i));

        // Automatically center the map fitting all markers on the screen
    }
}

// When the button is clicked, fetch the details about the entered flight ident.
$(document).ready(function(){
	$.ajax({
		type: 'GET',
		url: '/_getMarkers',
		data: { },
		success : function(result) {
			if (result.error) {
				alert('Failed to fetch');
				return;
			}
			addMarkers(result.markersList);
			console.log(result);
			//alert('Did not find any useful flights');
		}
	});
});



