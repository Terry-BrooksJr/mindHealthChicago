
$(function () {
	// Anchor Target Scroll Animation

	$('a[href*="#"]:not([href="#"])').click(function () {
		if (
			location.pathname.replace(/^\//, "") == this.pathname.replace(/^\//, "") &&
			location.hostname == this.hostname
		) {
			var target = $(this.hash);
			target = target.length ? target : $("[name=" + this.hash.slice(1) + "]");
			if (target.length) {
				$("html, body").animate(
					{
						scrollTop: target.offset().top - 62
					},
					600
				);
				return false;
			}
		}
	});

	// Header Shadow

	$(window).scroll(function () {
		var windowScroll = $(this).scrollTop();

		if (windowScroll > 304) {
			$(".navbar-fixed-top").addClass("shadow");
		} else {
			$(".navbar-fixed-top").removeClass("shadow");
		}
	});
});
var mySwiper = new Swiper(".swiper-container", {
	direction: "vertical",
	loop: true,
	pagination: ".swiper-pagination",
	grabCursor: true,
	speed: 1000,
	paginationClickable: true,
	parallax: true,
	autoplay: false,
	effect: "slide",
	mousewheelControl: 1
});
// PreLoader
jQuery.noConflict();
(function ($) {
	$(window).on("load", function () {
		// makes sure the whole site is loaded
		$("#status").fadeOut(); // will first fade out the loading animation
		$("#preloader").delay(300).fadeOut("slow"); // will fade out the white DIV that covers the website.
	});
})(jQuery);
// update footer copyright year

var today = new Date();
var year = today.getFullYear();
// Dynamic Copyright Date
var copyright = document.getElementById("copyright");
copyright.innerHTML = "© MindHealth " + year;


// Tooltip Enabler
$(function () {
	$('[data-toggle="tooltip"]').tooltip()
})

const phoneFormat = (input) => {
	//check if the string is a number (doesn’t include characters or letters) and not null or undefined\
	//check if the input is a string if not convert it into a string
	//check if the input length is 10 (us number is 10 digits)
	//if it is
	//format it to xxx-xxx-xxxx
	//if not check if it is less than 10
	//return error was not supplied enough numbers please pass a 10 digit number
	//if not check if length is greater than 10
	//return was supplied too many numbers please pass a 10 digit number
	//if not send something went wrong error for a catch all just in case
}
function numberValidator(number){
	const number = Document.getElementById('number')
	const pattern = new RegExp('1?\d{3}\d{3}\d{4}');
	if (number[0] == "1"){
		test_number = number.substring(1)
		search = test_number.search(pattern)
	} else {
		search = number.search(pattern)
	}
	if(search = -1){
		
	}
}
function numberValidator(number){
	const number = Document.getElementById('number')
	const pattern = new RegExp('1?\d{3}\d{3}\d{4}');
	if (number[0] == "1"){
		test_number = number.substring(1)``
def valid_phone(field):
number = field.data
number = number.translate(str.maketrans("", "", string.punctuation))
pattern = r"1?\d{3}\d{3}\d{4}"
number = number.strip()
if number[0] == "1":
	test_number = number[1:]
search = re.search(pattern, test_number)
    else:
search = re.search(pattern, number)
if search == None:
        raise ValidationError('Invaild Phone Number')
    else:
if len(search.group()) == 10:
	return True
else:
            raise ValidationError('Invaild Phone Number')