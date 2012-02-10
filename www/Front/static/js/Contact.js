$(function(){

	$("#map").gmap3({
		action: "addMarker",
		address: "16 rue de Bonne, Grenoble",
		map: {
			center: true,
			zoom: 16
		},
		infowindow: {
			options: {
				content: $("#map-tooltip-text").html()
			}
		}
	});

});