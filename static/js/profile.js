async function getProfileData(profileId) {
	return await $.get('/api/profiles/' + profileId + '/?format=json');
}


function main() {
    // Hide the data by defaukt
    $('#profile').css({
        display: 'none'
    });


	getProfileData(profileId).then(function (data) {
		// Set the username
		$('#username').html(data.user.username);

		// set the email
		$('#email').html(data.user.email);

		// set the image
		$('#profile_image')
			.attr('src', data.image)
			.css({
                height: 150
			});

        // Show the data
        $('#profile').css({
            display: 'block'
        });

        $('#loader').css({
            display: 'none'
        });
	})
}


main();
