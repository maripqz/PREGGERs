let get_input_dimensions = function() {
   let stage = $("select#stage").val()
   let breastfeeding = $("input#breastfeeding").is(":checked")
   let formula = $("input#formula").is(":checked")
   let solid = $("input#solid_foods").is(":checked")
   let meal_planning = $("input#meal_planning").is(":checked")
   let risks = $("input#risks").is(":checked")
   let weight = $("input#weight").is(":checked")
   let science = $("input#science").is(":checked")
   let diabetes = $("input#diabetes").is(":checked")
   let hypertension = $("input#hypertension").is(":checked")
   let obesity = $("input#obesity").is(":checked")
   // let reviews = $("input#reviews").val()
   // let rating = $("input#rating").val()
   // let bath = $("select#bath").val()
   // let view = $("select#view").val()
   // let instabook = $("select#instabook").val()
   // let prop_type = $("select#prop_type").val()

   return {'stage': stage,
           'breastfeeding': breastfeeding,
           'formula': formula,
           'solid': solid,
           'meal_planning': meal_planning,
           'risks': risks,
           'weight': weight,
           'science': science,
           'diabetes': diabetes,
           'hypertension': hypertension,
           'obesity': obesity,
          }
};
$(document).ready(function() {

    $("button#predict").click(function() {

        make_prediction(get_input_latlng());

    });

    $("select.dropdown").change(function() {

        make_prediction(get_input_latlng());

    });

    $("input.checkbox").click(function() {

        make_prediction(get_input_latlng());

    });

    // $("input#reviews").click(function() {
    //     make_prediction(get_input_latlng());
    //     document.getElementById("reviews_val").innerHTML = document.getElementById("reviews").value;
    // });
    //
    // $("input#rating").click(function() {
    //     make_prediction(get_input_latlng());
    //     document.getElementById("rating_val").innerHTML = document.getElementById("rating").value;
    // });
});
