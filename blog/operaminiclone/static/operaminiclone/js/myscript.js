$(document).ready(function() {
    // Handle button click
    $('#submit-comment-btn').click(function() {
       
            // Get the comment text from the input field
            var commentText = $('#comment-text').val();
        
            // Check if the comment is not empty
            if (commentText.trim() !== '') {
              // Create a data object to send to the server
              var data = {

                message: commentText
              };
              // Send the data to the server using AJAX
              $.ajax({
                type: "POST",
                url: "/addcomment", 
                data:{
                    'comment_text':commentText
                    },
                dataType: 'json', // Specify the data type you expect from the server
                success: function(response) {
                  if (response.success) {
                    // Display a success message or update the UI as needed
                    $('#result').html('Comment sent successfully');
                  } else {
                    // Display an error message from the server
                    $('#result').html('Error: ' + 'sssss');
                  }
                },
                error: function(xhr, status, error) {
                  // Handle any unexpected errors
                  $('#result').html('Error: ' + error);
                  console.error(xhr, status, error)
                }
              });
            } 
            else {
              // Display an error message if the comment is empty
              $('#result').html('Please enter a comment');
            }
          });
        });
   