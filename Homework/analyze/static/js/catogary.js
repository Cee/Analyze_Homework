$(document).ready(function(){
    $("select.main-catogary").change(function(){
    	// while(true){
        var mainCatogary=$("select.main-catogary").val();
        // var secondaryCatogary=$("select.secondary-catogary").val();
        // alert(mainCatogary);
        showSecondaryCatogary(mainCatogary);
        // showTertiaryCatogray(mainCatogary,secondaryCatogary);
    	// }
    });
    $("select.secondary-catogary").change(function(){
    	var mainCatogary=$("select.main-catogary").val();
	    var secondaryCatogary=$("select.secondary-catogary").val();
	    // alert(secondaryCatogary+mainCatogary);
	    showTertiaryCatogray(mainCatogary,secondaryCatogary);
    });
});

var catogary={
	"Baby Products":{
		"Diapering":["Diaper Bags"],
		"Nursery":["Bedding"]
	},
	"Beauty":{	
		"Bath & Body":["Bath","Bathing Accessories"],
		"Fragrance":["Sets"],
	  	"Hair Care":["Shampoos","Styling Products","Styling Tools"],
		"Makeup":["Body","Nails"],
		"Tools & Accessories":["Hair Coloring Tools"],
	},
	"Cell Phones & Accessories":{
		"Accessories":["Headsets","Smart Watches & Accessories"],
		"Cell Phones":["Contract Cell Phones"]
	},
	"Clothing & Accessories":{
		"Baby":["Baby Girls","Unisex"],
		"Boys":["Overalls","Pants","Shorts","Sleepwear & Robes","Suits & Sport Coats","Swim"],
		"Girls":["Accessories","Clothing Sets","Dresses","Leggings"],
		"Luggage & Bags":["Backpacks","Umbrellas"],
		"Men":["Jeans","Sweaters"],
		"Novelty & Special Use":["Sports Clothing","Work Wear & Uniforms","World Apparel"],
		"Women":["Active","Dresses","Jeans","Leggings","Skirts","Suits"]
	},
	"Electronics":{
		"Accessories & Supplies":["Microphones"],
		"Cell Phones & Accessories":["Mobile Broadband"],
		"Computers & Accessories":["Cables & Accessories","Computers & Accessories","External Components","Laptop & Netbook Computer Accessories"],
		"Television & Video":["Televisions"],
		"Video Game Consoles & Accessories":["PlayStation 4","Sony PSP","Xbox 360"]
	},
	"Health & Personal Care":{
		"Household Supplies":["Air Fresheners","Household Cleaning"]
	},
	"Home & Kitchen":{
		"Artwork":["Drawings"],
		"Bath":["Bathroom Accessories","Towels"],
		"Bedding":["Feather Beds"],
		"Furniture":["Home Office Furniture"],
		"Heating, Cooling & Air Quality":["Air Conditioners & Accessories","Space Heaters"],
		"Kids' Home Store":["Nursery Furniture"],
		"Kitchen & Dining":["Coffee, Tea & Espresso","Kitchen Utensils & Gadgets"],
		"Storage & Organization":["Baskets & Bins","Clothing & Closet Storage","Laundry Storage & Organization","Racks, Shelves & Drawers","Trash & Recycling"]
	},
	"Jewelry":{
		"Accessories":["Jewelry Boxes & Organizers"]
	},
	"Office Products":{
		"Office Electronics":["Calculators","Other Office Equipment"],
		"Office Furniture & Lighting":["Cabinets, Racks & Shelves","Carts & Stands","Chairs & Sofas","Desks & Workstations","Furniture Accessories","Office Lighting","Tables"]
	},
	"Patio, Lawn & Garden":{
		"Gardening":["Plant Containers"],
		"Mowers & Outdoor Power Tools":["Mowers & Tractors"]
	},
	"Pet Supplies":{
		"Birds":["Treats"],
	 	"Cats":["Memorials"],
	 	"Dogs":["Beds & Furniture","Carriers & Travel Products","Feeding & Watering Supplies","Food","Litter & Housebreaking","Memorials"],
	 	"Fish & Aquatic Pets":["Food","Water Treatments"],
	 	"Horses":["Food"],
	 	"Small Animals":["Health Supplies"]
	},
	"Shoes":{
		"Boys":["Athletic","Outdoor","Slippers","Sneakers","Uniform & School Shoes"],
		"Girls":["Outdoor","Slippers","Sneakers"],
		"Handbags":["Clutches","Cross-Body Bags","Evening Bags","Shoulder Bags"],
		"Men":["Outdoor","Sandals","Work & Safety"],
		"Shoe Care & Accessories":["Shoelaces"],
		"Women":["Outdoor","Sandals","Work & Safety"]
	},
	"Sports & Outdoors":{
		"Equestrian Sports":["Horse Care Equipment"]
	},
	"Tools & Home Improvement":{
		"Storage & Home Organization":["Garage Storage"]
	},
}

function showSecondaryCatogary(mainCatogary){
	switch (mainCatogary)
	{
		case "Baby Product":
	        $("select.secondary-catogary").empty();
//			$("select.secondary-catogary").append("<option value='all'>all</option>");
			$("select.secondary-catogary").append("<option value='Diapering'>Diapering</option>");
			$("select.secondary-catogary").append("<option value='Nursery'>Nursery</option>");
            $("#secondary-catogary").css("display","inline-block");
			break;
		case "Beauty":
	        $("select.secondary-catogary").empty();
//			$("select.secondary-catogary").append("<option value='all'>all</option>");
			$("select.secondary-catogary").append("<option value='Bath & Body'>Bath &amp; Body</option>");			
			$("select.secondary-catogary").append("<option value='Fragrance'>Fragrance</option>");			
			$("select.secondary-catogary").append("<option value='Hair Care'>Hair Care</option>");			
			$("select.secondary-catogary").append("<option value='Makeup'>Makeup</option>");			
			$("select.secondary-catogary").append("<option value='Tools & Accessories'>Tools &amp; Accessories</option>");		
            $("#secondary-catogary").css("display","inline-block");
			break;
		case "Cell Phones & Accessories":
	        $("select.secondary-catogary").empty();
//			$("select.secondary-catogary").append("<option value='all'>all</option>");
			$("select.secondary-catogary").append("<option value='Accessories'>Accessories</option>");			
			$("select.secondary-catogary").append("<option value='Cell Phones'>Cell Phones</option>");
            $("#secondary-catogary").css("display","inline-block");
			break;
		case "Clothing & Accessories":
	        $("select.secondary-catogary").empty();
//			$("select.secondary-catogary").append("<option value='all'>all</option>");
			$("select.secondary-catogary").append("<option value='Baby'>Baby</option>");			
			$("select.secondary-catogary").append("<option value='Boys'>Boys</option>");			
			$("select.secondary-catogary").append("<option value='Girls'>Girls</option>");			
			$("select.secondary-catogary").append("<option value='Luggage & Bags'>Luggage &amp; Bags</option>");			
			$("select.secondary-catogary").append("<option value='Men'>Men</option>");			
			$("select.secondary-catogary").append("<option value='Novelty & Special Use'>Novelty &amp; Special Use</option>");	
			$("select.secondary-catogary").append("<option value='Women'>Women</option>");
            $("#secondary-catogary").css("display","inline-block");
			break;
		case "Electronics":
	        $("select.secondary-catogary").empty();
//			$("select.secondary-catogary").append("<option value='all'>all</option>");
			$("select.secondary-catogary").append("<option value='Accessories & Supplies'>Accessories &amp; Supplies</option>");			
			$("select.secondary-catogary").append("<option value='Cell Phones & Accessories'>Cell Phones &amp; Accessories</option>");			
			$("select.secondary-catogary").append("<option value='Computers & Accessories'>Computers &amp; Accessories</option>");			
			$("select.secondary-catogary").append("<option value='Television & Video'>Television &amp; Video</option>");			
			$("select.secondary-catogary").append("<option value='Video Game Consoles & Accessories'>Video Game Consoles &amp; Accessories</option>");		
            $("#secondary-catogary").css("display","inline-block");
			break;
		case "Health & Personal Care":
	        $("select.secondary-catogary").empty();
			$("select.secondary-catogary").append("<option value='Household Supplies'>Household Supplies</option>");
            $("#secondary-catogary").css("display","inline-block");
			break;			
		case "Home & Kitchen":
	        $("select.secondary-catogary").empty();
//			$("select.secondary-catogary").append("<option value='all'>all</option>");
			$("select.secondary-catogary").append("<option value='Artwork'>Artwork</option>");			
			$("select.secondary-catogary").append("<option value='Bath'>Bath</option>");			
			$("select.secondary-catogary").append("<option value='Bedding'>Bedding</option>");			
			$("select.secondary-catogary").append("<option value='Furniture'>Furniture</option>");			
			$("select.secondary-catogary").append("<option value='Heating, Cooling & Air Quality'>Heating, Cooling &amp; Air Quality</option>");			
			$("select.secondary-catogary").append("<option value='Kids' Home Store'>Kids' Home Store</option>");			
			$("select.secondary-catogary").append("<option value='Kitchen & Dining'>Kitchen &amp; Dining</option>");			
			$("select.secondary-catogary").append("<option value='Storage & Organization'>Storage &amp; Organization</option>");
            $("#secondary-catogary").css("display","inline-block");
			break;
		case "Jewelry":
	        $("select.secondary-catogary").empty();
			$("select.secondary-catogary").append("<option value='Accessories'>Accessories</option>");
            $("#secondary-catogary").css("display","inline-block");
			break;
		case "Office Products":
	        $("select.secondary-catogary").empty();
//			$("select.secondary-catogary").append("<option value='all'>all</option>");
			$("select.secondary-catogary").append("<option value='Office Electronics'>Office Electronics</option>");			
			$("select.secondary-catogary").append("<option value='Office Furniture & Lighting'>Office Furniture &amp; Lighting</option>");
            $("#secondary-catogary").css("display","inline-block");
			break;
		case "Patio, Lawn & Garden":
	        $("select.secondary-catogary").empty();
//			$("select.secondary-catogary").append("<option value='all'>all</option>");
			$("select.secondary-catogary").append("<option value='Gardening'>Gardening</option>");			
			$("select.secondary-catogary").append("<option value='Mowers & Outdoor Power Tools'>Mowers &amp; Outdoor Power Tools</option>");
            $("#secondary-catogary").css("display","inline-block");
			break;
		case "Pet Supplies":
	        $("select.secondary-catogary").empty();
//			$("select.secondary-catogary").append("<option value='all'>all</option>");
			$("select.secondary-catogary").append("<option value='Birds'>Birds</option>");			
			$("select.secondary-catogary").append("<option value='Cats'>Cats</option>");			
			$("select.secondary-catogary").append("<option value='Dogs'>Dogs</option>");			
			$("select.secondary-catogary").append("<option value='Fish & Aquatic Pets'>Fish &amp; Aquatic Pets</option>");		
			$("select.secondary-catogary").append("<option value='Horses'>Horses</option>");			
			$("select.secondary-catogary").append("<option value='Small Animals'>Small Animals</option>");
            $("#secondary-catogary").css("display","inline-block");
			break;
		case "Shoes":
	        $("select.secondary-catogary").empty();
//			$("select.secondary-catogary").append("<option value='all'>all</option>");
			$("select.secondary-catogary").append("<option value='Boys`'>Boys`</option>");			
			$("select.secondary-catogary").append("<option value='Girls'>Girls</option>");			
			$("select.secondary-catogary").append("<option value='Handbags'>Handbags</option>");			
			$("select.secondary-catogary").append("<option value='Men'>Men</option>");			
			$("select.secondary-catogary").append("<option value='Shoe Care & Accessories'>Shoe Care &amp; Accessories</option>");			
			$("select.secondary-catogary").append("<option value='Women'>Women</option>");
            $("#secondary-catogary").css("display","inline-block");
			break;
		case "Sports & Outdoors":
	        $("select.secondary-catogary").empty();
			$("select.secondary-catogary").append("<option value='Equestrian Sports'>Equestrian Sports</option>");
            $("#secondary-catogary").css("display","inline-block");
			break;	
		case "Tools & Home Improvement":
	        $("select.secondary-catogary").empty();
			$("select.secondary-catogary").append("<option value='Storage & Home Organization'>Storage &amp; Home Organization</option>");
            $("#secondary-catogary").css("display","inline-block");
			break;
		default:
	        $("select.secondary-catogary").empty();
            $("#secondary-catogary").css("display","none");
			break;
	}
}

function showTertiaryCatogray(mainCatogary,secondaryCatogary){
    for(var mainItem in catogary){
    	if (mainItem==mainCatogary){
    		// alert(mainItem);
    		for (var secondaryItem in catogary[mainItem]){
		        // $("select.tertiary-catogary").empty();
    			// alert(secondaryItem + " "+secondaryCatogary);
    			if (secondaryItem===secondaryCatogary){   				
					$("select.tertiary-catogary").append("<option value='all'>all</option>");	
    				for (var item in catogary[mainItem][secondaryItem]){
    					// alert(catogary[mainItem][secondaryItem][item]);
    					$("select.tertiary-catogray").append("<option value='"+catogary[mainItem][secondaryItem][item]+"'>"+catogary[mainItem][secondaryItem][item]+"</option>");    					
    				}
    				$("#tertiary-catogray").css("display","inline-block");
    				//alert();
    				break;
    			}
    		}
    	}
    }
}