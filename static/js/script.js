$(".compile-button").click(function() {

    var texto = $(".text-box").val();
  
    $.ajax({
      url: "/mi-ruta",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({texto: texto}),
      success: function(response) {
        $(".resultado").val(response);
      },
      error: function(xhr, status, error) {
        console.error("Error en la solicitud:", error);
      }
    });
  });
  
  