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
      map: map
    });
	map.addListener('rightclick', function(e) {
        createWindow(e);
    });
}

function createWindow(e) {
    marker.setPosition(e.latLng);
    
    //set position data
    var latitude = e.latLng.lat();
    var longitude = e.latLng.lng();
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

function saveData() {
    var name = escape(document.getElementById('description').value);
    var type = document.getElementById('type').value;
    var latlng = marker.getPosition();
    messagewindow = new google.maps.InfoWindow({
        content: document.getElementById('message')
    });
        google.maps.event.addListener(map,'click',function(){
        window.location.reload();
   // then, remove the infowindows name from the array
});
    infowindow.close();
        google.maps.event.addListener(messagewindow,'closeclick',function(){
        window.location.reload();
   // then, remove the infowindows name from the array
});
    messagewindow.open(map, marker);
}





