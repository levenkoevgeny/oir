const EMPLOYEE_KIND_CADET = 1
const EMPLOYEE_KIND_PPS = 2


$("#employee_kind_id").change(function () {

    $("#cadet_data_div_id, #subdivision_div_id").css("display", "none");
    $("#subdivision_id, #faculty_id, #course_id").prop("required", false);

    let selected_id = $(this).val();

    if (selected_id == EMPLOYEE_KIND_CADET) {
        $("#cadet_data_div_id").css("display", "block");
        $("#faculty_id, #course_id").prop("required", true);
    } else if (selected_id == EMPLOYEE_KIND_PPS) {
        $("#subdivision_div_id").css("display", "block");
        $("#subdivision_id").prop("required", true);
    }

});

$(".check_with_extra_data").change(function () {
    let this_name = $(this).attr('name');
    if ($(this).is(':checked')) {
        $(`#${this_name}_extra_div_id`).css("display", "block");
        $(`#${this_name}_extra_input_id`).prop("required", true).prop("disabled", false);
    } else {
        $(`#${this_name}_extra_div_id`).css("display", "none");
        $(`#${this_name}_extra_input_id`).prop("required", false).prop("disabled", true);
    }
});


$(".answer_radio").change(function () {
    let this_name = $(this).attr('name');
    // console.log('fuuu');
    if ($(this).hasClass('radio_with_extra_data')) {
        // console.log('fff');
        // console.log(this_name);
        $(`#${this_name}_extra_div_id`).css("display", "block");
        $(`#${this_name}_extra_input_id`).prop("required", true).prop("disabled", false);
    } else {
        $(`#${this_name}_extra_div_id`).css("display", "none");
        $(`#${this_name}_extra_input_id`).prop("required", false).prop("disabled", true);
    }
});