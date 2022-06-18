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