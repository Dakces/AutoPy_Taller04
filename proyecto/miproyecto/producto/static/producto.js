$(function () {
  var edit_url = $("#edit_record").attr("data-url");
  var view_url = $("#view_record").attr("data-url");
  var delete_url = $("#delete_record").attr("data-url");
  var current_id=0;
  
  
  function enableButtons(recordId){
    current_id = parseInt(recordId);
    $("#edit_record").removeClass("disabled");
    $("#view_record").removeClass("disabled");
    $("#delete_record").removeClass("disabled");
    $("#edit_record").prop("href",edit_url+recordId);
    $("#view_record").prop("href",view_url+recordId);
    $("#delete_modal_form").prop("action",delete_url+recordId);
  }
  
  function disableButtons(){
    current_id=0;
    $("#edit_record").addClass("disabled");
    $("#view_record").addClass("disabled");
    $("#delete_record").addClass("disabled");
    $("#edit_record").prop("href",edit_url);
    $("#view_record").prop("href",view_url);
    $("#delete_modal_form").prop("action",delete_url);
  }
  
  $('#datatable tbody').on( 'click', 'tr', function () {
    console.log($(this).attr("data-not-click"));
    if (typeof $(this).attr("data-not-click") =="undefined"){
      if ( $(this).hasClass('selected') ) {
          $(this).removeClass('selected');
          disableButtons();
      }
      else {
          //datatable.$('tr.selected').removeClass('selected');
          $('#datatable tr.selected').removeClass('selected');
          $(this).addClass('selected');
          enableButtons($(this).attr("data-id"));
      }
    }

  });
  
});