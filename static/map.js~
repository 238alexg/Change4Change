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
	map.addListener('rightclick', function(e) {
    marker.setPosition(e.latLng);
    
    var latitude = e.latLng.lat();
    var longitude = e.latLng.lng();
    console.log("Latitude: " + latitude +'\n' +"Longitude: " + longitude);
    createWindow();


  });
}

function createWindow() {
    infowindow = new google.maps.InfoWindow;
    var formData = document.getElementById('form');
    infowindow.setContent(formData);
    infowindow.open(map, marker);
    messagewindow = new google.maps.InfoWindow({
        content: document.getElementById('message')
    });
}

function saveData() {
    var name = escape(document.getElementById('name').value);
    var address = escape(document.getElementById('address').value);
    var type = document.getElementById('type').value;
    var latlng = marker.getPosition();
    messagewindow.open(map, marker);
}





