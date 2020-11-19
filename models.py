# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountPCountry(models.Model):
    country_id = models.CharField(primary_key=True, max_length=250)
    sort_name = models.CharField(max_length=250)
    country = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'account_p_country'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class BlogComment(models.Model):
    blog_comment_id = models.AutoField(primary_key=True)
    queries = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_comment'


class BusinessCitationCitation(models.Model):
    website = models.CharField(unique=True, max_length=200)
    citation_profile_url = models.CharField(max_length=200)
    citation_date = models.DateField(blank=True, null=True)
    citation_expiary_date = models.DateField(blank=True, null=True)
    citation_validity = models.DateField(blank=True, null=True)
    citation_status = models.IntegerField()
    citation_website = models.ForeignKey('BusinessCitationCitationWebsite', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_citation_citation'


class BusinessCitationCitationWebsite(models.Model):
    citation_website_id = models.AutoField(primary_key=True)
    citation_website = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'business_citation_citation_website'


class BusinessDetailedInformation(models.Model):
    business_title = models.CharField(max_length=256)
    business_description = models.CharField(max_length=256)
    no_of_employee = models.IntegerField(blank=True, null=True)
    annual_turn_over = models.IntegerField(blank=True, null=True)
    total_income = models.IntegerField(blank=True, null=True)
    ownership_type = models.CharField(max_length=255)
    local_time = models.TimeField(blank=True, null=True)
    company_founded_year = models.PositiveSmallIntegerField(blank=True, null=True)
    company_founded_date = models.PositiveSmallIntegerField(blank=True, null=True)
    company_founded_month = models.CharField(max_length=255)
    price = models.IntegerField(blank=True, null=True)
    keywords = models.CharField(max_length=256)
    language = models.CharField(max_length=256)
    sector = models.CharField(max_length=256)
    business_category = models.ForeignKey('PBusinessCategory', models.DO_NOTHING)
    business_sub_category = models.ForeignKey('PBusinessSubCategory', models.DO_NOTHING)
    city = models.ForeignKey('PCity', models.DO_NOTHING, blank=True, null=True)
    company_type = models.ForeignKey('PCompanyType', models.DO_NOTHING)
    currency_type = models.ForeignKey('PCurrencyType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_detailed_information'


class BusinessDetailedInformationCompanyImage(models.Model):
    businessdetailedinformation = models.ForeignKey(BusinessDetailedInformation, models.DO_NOTHING)
    companyimages = models.ForeignKey('ProfilebuilderCompanyimages', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'business_detailed_information_company_image'
        unique_together = (('businessdetailedinformation', 'companyimages'),)


class BusinessDetailedInformationCompanyLogo(models.Model):
    businessdetailedinformation = models.ForeignKey(BusinessDetailedInformation, models.DO_NOTHING)
    companylogo = models.ForeignKey('ProfilebuilderCompanylogo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'business_detailed_information_company_logo'
        unique_together = (('businessdetailedinformation', 'companylogo'),)


class BusinessInformation(models.Model):
    business_title = models.CharField(max_length=256)
    business_description = models.CharField(max_length=256)
    business_country = models.CharField(max_length=256)
    business_tag = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'business_information'


class CitationParams(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    day = models.CharField(max_length=255, blank=True, null=True)
    month = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(unique=True, max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    confirm_password = models.CharField(max_length=255, blank=True, null=True)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    business_title = models.CharField(max_length=255, blank=True, null=True)
    business_desc = models.TextField(blank=True, null=True)
    business_country = models.CharField(max_length=255, blank=True, null=True)
    business_category = models.CharField(max_length=255, blank=True, null=True)
    categories = models.CharField(max_length=255, blank=True, null=True)
    years_of_estd = models.CharField(max_length=255, blank=True, null=True)
    no_of_emp = models.CharField(max_length=255, blank=True, null=True)
    annual_turn_over = models.CharField(max_length=255, blank=True, null=True)
    total_income = models.CharField(max_length=255, blank=True, null=True)
    currency_type = models.CharField(max_length=255, blank=True, null=True)
    ownership_type = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    local_time = models.DateTimeField(blank=True, null=True)
    blog = models.TextField(blank=True, null=True)
    faxnumber = models.CharField(max_length=80, blank=True, null=True)
    twitter = models.CharField(max_length=25, blank=True, null=True)
    skype = models.CharField(max_length=25, blank=True, null=True)
    msn = models.CharField(max_length=25, blank=True, null=True)
    business_tag = models.CharField(max_length=25, blank=True, null=True)
    company_founded_month = models.IntegerField(blank=True, null=True)
    company_founded_year = models.IntegerField(blank=True, null=True)
    company_email = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    youtube = models.CharField(max_length=50, blank=True, null=True)
    pinterest = models.CharField(max_length=50, blank=True, null=True)
    linkedin = models.CharField(db_column='linkedIn', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keywords = models.TextField(blank=True, null=True)
    designation = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    sector = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    keyword = models.CharField(max_length=155, blank=True, null=True)
    image_path = models.CharField(max_length=45, blank=True, null=True)
    sub_category = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citation_params'


class ContactInformation(models.Model):
    email = models.CharField(unique=True, max_length=254)
    phone = models.CharField(max_length=128)
    faxnumber = models.CharField(max_length=255)
    website = models.CharField(unique=True, max_length=255)
    street_address = models.CharField(max_length=256)
    pincode = models.CharField(max_length=256)
    city = models.ForeignKey('PCity', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('PCountry', models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('PLocation', models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey('PState', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_information'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ProfilebuilderUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FirstAppPState1(models.Model):
    state_id = models.IntegerField()
    state = models.CharField(max_length=30)
    country_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'first_app_p_state1'


class Frequency(models.Model):
    frequency_id = models.AutoField(primary_key=True)
    frequency = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frequency'


class KeyfinderCustomercompetitor(models.Model):
    domain_name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'keyfinder_customercompetitor'


class KeyfinderWebsitekeyword(models.Model):
    keyword_value = models.CharField(unique=True, max_length=255)
    is_focus_keyword = models.IntegerField()
    website = models.ForeignKey('ProfilebuilderCustomerwebsite', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyfinder_websitekeyword'


class Keyword(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    website_id = models.IntegerField(blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    keyword = models.CharField(unique=True, max_length=255, blank=True, null=True)
    call_success = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyword'


class LDirectoryDetail(models.Model):
    directory_id = models.IntegerField(primary_key=True)
    domain_authority = models.IntegerField(blank=True, null=True)
    page_authority = models.IntegerField(blank=True, null=True)
    spam_score = models.IntegerField(blank=True, null=True)
    domain_age = models.TextField(blank=True, null=True)
    is_domain_up = models.IntegerField(blank=True, null=True)
    is_domain_expired = models.IntegerField(blank=True, null=True)
    majestic_trustflow = models.IntegerField(blank=True, null=True)
    alexa_global_ranking = models.IntegerField(blank=True, null=True)
    alexa_traffic_country = models.IntegerField(blank=True, null=True)
    majestic_citationflow = models.IntegerField(blank=True, null=True)
    niche = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    is_https = models.IntegerField(blank=True, null=True)
    is_dofollow = models.IntegerField(blank=True, null=True)
    update_date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l_directory_detail'


class LDirectoryList(models.Model):
    directory_id = models.AutoField(primary_key=True)
    website = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l_directory_list'


class MyPreference(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_preference'


class PBusinessCategory(models.Model):
    business_category_id = models.AutoField(primary_key=True)
    business_category = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_business_category'


class PBusinessCitation(models.Model):
    website = models.CharField(max_length=255, blank=True, null=True)
    business_citation = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_business_citation'


class PBusinessSubCategory(models.Model):
    business_sub_category_id = models.AutoField(primary_key=True)
    business_sub_category = models.CharField(max_length=455, blank=True, null=True)
    business_category = models.ForeignKey(PBusinessCategory, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_business_sub_category'


class PCity(models.Model):
    city_id = models.AutoField(primary_key=True)
    country = models.ForeignKey('PCountry', models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey('PState', models.DO_NOTHING, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_city'


class PCompanyType(models.Model):
    company_type_id = models.AutoField(primary_key=True)
    company_type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_company_type'


class PCountry(models.Model):
    country_id = models.AutoField(primary_key=True)
    shortname = models.CharField(unique=True, max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_country'


class PCurrency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    currency = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_currency'


class PCurrencyType(models.Model):
    currency_type_id = models.AutoField(primary_key=True)
    currency_type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_currency_type'


class PEmployees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_strength = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_employees'


class PLocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    state = models.ForeignKey('PState', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(PCountry, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(PCity, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_location'


class PLogo(models.Model):
    logo_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_logo'


class POffice(models.Model):
    office_type_id = models.AutoField(primary_key=True)
    office_type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_office'


class POfficeType(models.Model):
    office_type_id = models.AutoField(primary_key=True)
    office_type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_office_type'


class PState(models.Model):
    state_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(PCountry, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_state'


class PWebsite(models.Model):
    website_name = models.CharField(max_length=255, blank=True, null=True)
    website_link = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_website'


class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    salutation = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personal_information'


class Plan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    plan = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan'


class ProfilebuilderCompanyimages(models.Model):
    images = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'profilebuilder_companyimages'


class ProfilebuilderCompanylogo(models.Model):
    images = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'profilebuilder_companylogo'


class ProfilebuilderCustomer(models.Model):
    user = models.OneToOneField('ProfilebuilderUser', models.DO_NOTHING, primary_key=True)
    email = models.CharField(unique=True, max_length=254)
    name = models.CharField(max_length=256)
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    phone = models.CharField(max_length=128)
    customer_business_detailed_info = models.ForeignKey(BusinessDetailedInformation, models.DO_NOTHING, blank=True, null=True)
    customer_business_info = models.ForeignKey(BusinessInformation, models.DO_NOTHING, blank=True, null=True)
    customer_contact_info = models.ForeignKey(ContactInformation, models.DO_NOTHING, blank=True, null=True)
    customer_personal_info = models.ForeignKey(PersonalInformation, models.DO_NOTHING, blank=True, null=True)
    customer_social_media_info = models.ForeignKey('SocialMediaInformation', models.DO_NOTHING, blank=True, null=True)
    customer_website = models.OneToOneField('ProfilebuilderCustomerwebsite', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profilebuilder_customer'


class ProfilebuilderCustomerwebsite(models.Model):
    website_name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'profilebuilder_customerwebsite'


class ProfilebuilderProfile(models.Model):
    businessdetailedinfo = models.ForeignKey(BusinessDetailedInformation, models.DO_NOTHING, blank=True, null=True)
    businessinfo = models.ForeignKey(BusinessInformation, models.DO_NOTHING)
    contactinfo = models.ForeignKey(ContactInformation, models.DO_NOTHING)
    personalinfo = models.ForeignKey(PersonalInformation, models.DO_NOTHING)
    socialmediainformation = models.ForeignKey('SocialMediaInformation', models.DO_NOTHING)
    user = models.ForeignKey(ProfilebuilderCustomer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profilebuilder_profile'


class ProfilebuilderUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    is_customer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profilebuilder_user'


class ProfilebuilderUserGroups(models.Model):
    user = models.ForeignKey(ProfilebuilderUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profilebuilder_user_groups'
        unique_together = (('user', 'group'),)


class ProfilebuilderUserUserPermissions(models.Model):
    user = models.ForeignKey(ProfilebuilderUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profilebuilder_user_user_permissions'
        unique_together = (('user', 'permission'),)


class QIndustryQuestionAnswer(models.Model):
    iqa_id = models.AutoField(primary_key=True)
    queries = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'q_industry_question_answer'


class QOtherQuestionAnswer(models.Model):
    oqa_id = models.AutoField(primary_key=True)
    queries = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'q_other_question_answer'


class RankCheckFrequency(models.Model):
    frequency_id = models.IntegerField(primary_key=True)
    frequency = models.CharField(max_length=255, blank=True, null=True)
    plan_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rank_check_frequency'


class RankTracker(models.Model):
    website_id = models.CharField(max_length=255, blank=True, null=True)
    keyword_id = models.CharField(max_length=255, blank=True, null=True)
    last_rank = models.CharField(max_length=255, blank=True, null=True)
    last_date = models.DateField(blank=True, null=True)
    present_rank = models.CharField(max_length=255, blank=True, null=True)
    present_date = models.DateField(blank=True, null=True)
    rank_difference = models.CharField(max_length=255, blank=True, null=True)
    result_url = models.CharField(max_length=500, blank=True, null=True)
    local_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rank_tracker'


class RankTrackerAggregate(models.Model):
    website_id = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    keyword_id = models.CharField(max_length=255, blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    rank_difference = models.CharField(max_length=255, blank=True, null=True)
    number_3_months_back_rank = models.CharField(db_column='3_Months_back_rank', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_months_back_date = models.DateTimeField(db_column='3_Months_back_date', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_months_back_rank = models.CharField(db_column='2_Months_back_rank', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_months_back_date = models.DateTimeField(db_column='2_Months_back_date', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_month_back_rank = models.CharField(db_column='1_Month_back_rank', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_month_back_date = models.DateTimeField(db_column='1_Month_back_date', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_weeks_back_rank = models.CharField(db_column='2_weeks_back_rank', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2_weeks_back_date = models.DateTimeField(db_column='2_weeks_back_date', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_week_back_rank = models.CharField(db_column='1_week_back_rank', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_week_back_date = models.DateTimeField(db_column='1_week_back_date', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    local_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rank_tracker_aggregate'


class SerpRankfactor(models.Model):
    website_id = models.IntegerField(primary_key=True)
    domain_authority = models.IntegerField(blank=True, null=True)
    page_authority = models.IntegerField(blank=True, null=True)
    total_backlinks = models.CharField(max_length=55, blank=True, null=True)
    quality_backlinks = models.CharField(max_length=55, blank=True, null=True)
    percentage_quality_backlinks = models.IntegerField(blank=True, null=True)
    moz_trust = models.TextField(blank=True, null=True)
    spam_score = models.IntegerField(blank=True, null=True)
    offpage_seo_score = models.IntegerField(blank=True, null=True)
    alexa_global_ranking = models.IntegerField(blank=True, null=True)
    majestic_trust_flow = models.IntegerField(blank=True, null=True)
    majestic_citatiion_flow = models.IntegerField(blank=True, null=True)
    majestic_indexed_url = models.IntegerField(blank=True, null=True)
    majestic_dofollow_backlinks = models.IntegerField(blank=True, null=True)
    majestic_nofollow_backlinks = models.IntegerField(blank=True, null=True)
    domain_name = models.CharField(max_length=55, blank=True, null=True)
    domain_purchase_date = models.CharField(max_length=55, blank=True, null=True)
    domain_age = models.CharField(max_length=55, blank=True, null=True)
    domain_updated_date = models.CharField(max_length=55, blank=True, null=True)
    domain_expiration_date = models.CharField(max_length=55, blank=True, null=True)
    registrar = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serp_rankfactor'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthPartial(models.Model):
    token = models.CharField(max_length=32)
    next_step = models.PositiveSmallIntegerField()
    backend = models.CharField(max_length=32)
    data = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(ProfilebuilderUser, models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)


class SocialMediaInformation(models.Model):
    digital_marketing_email_id = models.CharField(unique=True, max_length=254)
    password = models.CharField(max_length=50)
    skype = models.CharField(unique=True, max_length=255)
    msn = models.CharField(unique=True, max_length=255)
    facebook = models.CharField(unique=True, max_length=255)
    linkedin = models.CharField(db_column='linkedIn', unique=True, max_length=255)  # Field name made lowercase.
    pinterest = models.CharField(unique=True, max_length=255)
    twitter = models.CharField(unique=True, max_length=255)
    blog = models.CharField(unique=True, max_length=255)
    youtube = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'social_media_information'


class SpComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_comment'


class SpCountry(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_country'


class SpDate(models.Model):
    date_id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    day_of_week_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_date'


class SpDayOfWeek(models.Model):
    day_of_week_id = models.IntegerField(primary_key=True)
    day_of_week = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_day_of_week'


class SpFestival(models.Model):
    festival_id = models.AutoField(primary_key=True)
    festival = models.TextField(blank=True, null=True)
    date_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_festival'


class SpGreetingPhrase(models.Model):
    greeting_phrase_id = models.IntegerField(primary_key=True)
    greeting_phrase = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_greeting_phrase'


class SpImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_url = models.TextField(db_column='Image_url', blank=True, null=True)  # Field name made lowercase.
    post_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_image'


class SpInternationalDay(models.Model):
    international_day_id = models.AutoField(primary_key=True)
    international_day = models.TextField(blank=True, null=True)
    date_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_international_day'


class SpNationalHoliday(models.Model):
    national_holiday = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    date_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_national_holiday'


class SpPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    festival_id = models.IntegerField(blank=True, null=True)
    post_type_id = models.IntegerField(blank=True, null=True)
    international_day_id = models.IntegerField(blank=True, null=True)
    image_id = models.IntegerField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    national_id = models.IntegerField(blank=True, null=True)
    day_of_week_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_post'


class SpPostType(models.Model):
    post_type_id = models.IntegerField(primary_key=True)
    post_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_post_type'


class SpState(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_state'


class SpWebsitePost(models.Model):
    website_id = models.IntegerField(blank=True, null=True)
    date_id = models.DateField(blank=True, null=True)
    post_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_website_post'


class SpecialMaster(models.Model):
    day = models.CharField(max_length=255, blank=True, null=True)
    special_name = models.TextField(blank=True, null=True)
    rocognize_by = models.CharField(max_length=255, blank=True, null=True)
    local_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'special_master'


class State(models.Model):
    state_id = models.IntegerField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'


class Website(models.Model):
    website_id = models.AutoField(primary_key=True)
    website = models.CharField(unique=True, max_length=255, blank=True, null=True)
    logo_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website'


class WebsiteFields(models.Model):
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    offer_type = models.CharField(max_length=255, blank=True, null=True)
    registered_by = models.CharField(max_length=255, blank=True, null=True)
    employees_strength = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    industry_type = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)
    currency_type = models.CharField(max_length=255, blank=True, null=True)
    sub_category = models.CharField(max_length=255, blank=True, null=True)
    office_type = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_fields'


class WebsiteKeywordTable(models.Model):
    website_id = models.CharField(max_length=255, blank=True, null=True)
    keyword_id = models.CharField(max_length=255, blank=True, null=True)
    call_success = models.IntegerField(blank=True, null=True)
    local_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_keyword_table'
