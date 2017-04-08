var map;
//#141414
function initMap() {

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
      map: map,
    }),
    infowindow = new google.maps.InfoWindow;
	map.addListener('rightclick', function(e) {
    marker.setPosition(e.latLng);
    infowindow.setContent("Latitude: " + e.latLng.lat() +
      "<br>" + "Longitude: " + e.latLng.lng());
    infowindow.open(map, marker);
  });
}
