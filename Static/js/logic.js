
document.getElementById("filter-btn").onclick = function() {
    //First things first, we need our text:
    list = []
    var bedrooms = document.getElementById("Bedrooms").value; //.value gets input values
    var full_bathrooms = document.getElementById("Full_Bathrooms").value;
    var half_bathrooms = document.getElementById("Half_Bathrooms").value;
    var living_area = document.getElementById("Living_Area_sq_ft").value;
    var quality = document.getElementById("Construction_Quality").value;
    var condition = document.getElementById("Condition_Score").value;
    var garage = document.getElementById("Garage").value;
    var basement = document.getElementById("Finished_Basement").value;
    var land = document.getElementById("Total_Land_sq_").value;
    var age = document.getElementById("House_Age").value;

    var final_list = [bedrooms,full_bathrooms,half_bathrooms,living_area,quality,
    condition,garage,basement,land,age];
    console.log(final_list);
    
    var load  = final_list.join(); 
    console.log(load)

    $.get($SCRIPT_ROOT + `/Calculator`, {
        input: JSON.stringify(load)
    }, function(data){
        console.log(data)
        $( "#myText" ).append("h6").text(data);
    });
}

// function sellprice(final_list) {
//     var outcome = document.getElementById("myText");
//     var url = `/Calculator/${final_list}`;

//     d3.json(url).then(function (Outcome) {

//         var data1 = Outcome;
//         outcome.html("");

//         outcome.append(data1)
//     });
// };

// sellprice();