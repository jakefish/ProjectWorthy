############################  Check if user is admin

def user_is_admin(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Check if user is admin (site owner) this will be used for view verification across the project
    """
    actual_decorator = custom_user_passes_test(
        lambda u: get_worker(u).is_admin_user(),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

############################  Login User

def login(request):
    """
    Authenticates user and logs them into the site
    """
    redirect_to = "This field will redirect user to a login page"
    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():
            #Check if the user is logged in or not and provide proper handling
            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)
    context = {}  #This will hold the context to be returned
    return TemplateResponse(request, template_name, context)  #Render request to view and proper template


############################  Generate Random Workout

def generate_random_workout(self, workout_list, move_set):
    """
    Will take prexisting workouts and movements and generate a random workout.
    """
    random_workout = []
    for workout in workout_list:
        random_workout.append(random_workout)

    for movement in moveset:
        random_workout.append(random_moveset)

    rand_number = 0
    for workout in random_workout:
        import random
        rand_number = random.random()

    generated_workout = random_workout[rand_number]

############################  Create or save notes
def create_or_submit_notes(self, request):
    """Takes request and updates or creates new user note object """

    if request.method == "POST":
        if NotesForm.is_valid():
            NotesForm.save()
            return HttpResponse("Success")
    if request.method == "GET"
        notes_form = NotesForm()

    context = {NotesForm(): 'NotesForm'}

    return TemplateResponse(template, context, request)



######## Graphs

def generate_color_list(colour_range = 25):
    """Generate Colors """
	for i in range(colour_range):
		random_color = Color(rgb=(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)))
		color.append(random_color.hex)
	return color

def get_partcount_chart_range():
    """Get axis range best on user times """
	if User.objects.count():
		query_set = User.objects.all().order_by("-shift_datetime")
		end_time = query_set[0].shift_datetime
		start_time = query_set.reverse()[0].shift_datetime
	else:
		end_time = dt.now()
		start_time = end_time - timedelta(days=1)

	end_time = tm.mktime(end_time.timetuple())*1000
	start_time = tm.mktime(start_time.timetuple())*1000
	return start_time, end_time


#### display graph data
def display_charts(self, request, *args, **kwargs):
		start_time, end_time = get_partcount_chart_range()
        user = User.objects.all()
        dates = User.dates.objects.all()


		data, room_data = {}, {}
		dates           = []
		context = super(DataRange, self).get_context_data(**kwargs)

		chart_settings = {
			"x_is_date": True,
			"x_axis_format": "%d %b %Y",
			'show_legend': True,
			"show_labels": False,
			"reduce_x_ticks": True,
			"jquery_on_ready": True,
			"resize": True
		}

		"""MULTI BAR CHART"""
		multiple_bar_char  = multiBarChart(name="multi-bar-chart", **chart_settings)

		"""STACKED AREA CHART"""
		stacked_chart = stackedAreaChart(name="stacked-area-chart", **chart_settings)

		"""LINE WITH FOCUS CHART"""
		line_with_focus_chart = lineWithFocusChart(name="line-with-focus-chart", **chart_settings)

		try:
			datepicker_start  = unicodedata.normalize('NFKD', request.POST.get('datepicker_start')).encode('ascii', 'ignore')
			datepicker_end    = unicodedata.normalize('NFKD', request.POST.get('datepicker_end')).encode('ascii', 'ignore')
		except TypeError:
			context.update({
				'error': "Please make sure all date fields are filled out",
				'locations': locations_data,
				'start_time': start_time,
				'end_time': end_time,
				'shifts': shifts,
				'buildings': buildings
			})

			return render(request, self.template_name, context)


		date_picker_range = [dt.strptime(datepicker_start, '%Y/%m/%d %I:%M %p'), dt.strptime(datepicker_end, '%Y/%m/%d %I:%M %p')]
		location_picker   = request.POST.getlist('location_picker')
		location_picker   = map(int, location_picker)
