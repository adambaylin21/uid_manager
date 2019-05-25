$(document).on('click', ".add_uid", function () {
	var uid = $('#log_uid').val()
    $("#log_uid").val("");
    $.ajax({
        type: 'post',
        url: '/logic/add_uid',
        data: {add_uid: JSON.stringify(uid)},
        success: function (resp) {
            $(".status_logic").css("display", "inline-block");
            $('#total_add').replaceWith(resp.data);
            setTimeout(
              function() 
              {
                $(".status_logic").css("display", "none");
              }, 5000);
            }
      });

});
$(document).on('click', ".del_all", function () {
    $.ajax({
        type: 'post',
        url: '/logic/del_all',
        success: function (resp) {
            $(".status_logic").css("display", "inline-block");
            $('#total_add').replaceWith(resp.data);
            setTimeout(
              function() 
              {
                $(".status_logic").css("display", "none");
              }, 5000);
            }
      });

});