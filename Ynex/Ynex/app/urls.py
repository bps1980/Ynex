from . import views
from django.urls import path

appname = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('accordionscollpase', views.accordionscollpase, name='accordionscollpase'),
    path('addproducts', views.addproducts, name='addproducts'),
    path('alerts', views.alerts, name='alerts'),
    path('apexareacharts', views.apexareacharts, name='apexareacharts'),
    path('apexbarcharts', views.apexbarcharts, name='apexbarcharts'),
    path('apexboxplotcharts', views.apexboxplotcharts, name='apexboxplotcharts'),
    path('apexbubblecharts', views.apexbubblecharts, name='apexbubblecharts'),
    path('apexcandlestickcharts', views.apexcandlestickcharts, name='apexcandlestickcharts'),
    path('apexcolumncharts', views.apexcolumncharts, name='apexcolumncharts'),
    path('apexheatmapcharts', views.apexheatmapcharts, name='apexheatmapcharts'),
    path('apexlinecharts', views.apexlinecharts, name='apexlinecharts'),
    path('apexmixedcharts', views.apexmixedcharts, name='apexmixedcharts'),
    path('apexpiecharts', views.apexpiecharts, name='apexpiecharts'),
    path('apexpolarareacharts', views.apexpolarareacharts, name='apexpolarareacharts'),
    path('apexradarcharts', views.apexradarcharts, name='apexradarcharts'),
    path('apexradialbarcharts', views.apexradialbarcharts, name='apexradialbarcharts'),
    path('apexrangeareacharts', views.apexrangeareacharts, name='apexrangeareacharts'),
    path('apexscattercharts', views.apexscattercharts, name='apexscattercharts'),
    path('apextimelinecharts', views.apextimelinecharts, name='apextimelinecharts'),
    path('apextreemapcharts', views.apextreemapcharts, name='apextreemapcharts'),
    path('avatars', views.avatars, name='avatars'),
    path('badge', views.badge, name='badge'),
    path('blog', views.blog, name='blog'),
    path('blogcreate', views.blogcreate, name='blogcreate'),
    path('blogdetails', views.blogdetails, name='blogdetails'),
    path('borders', views.borders, name='borders'),
    path('breadcrumb', views.breadcrumb, name='breadcrumb'),
    path('breakpoints', views.breakpoints, name='breakpoints'),
    path('buttongroup', views.buttongroup, name='buttongroup'),
    path('buttons', views.buttons, name='buttons'),
    path('cards', views.cards, name='cards'),
    path('carousel', views.carousel, name='carousel'),
    path('cart', views.cart, name='cart'),
    path('chartjscharts', views.chartjscharts, name='chartjscharts'),
    path('chat', views.chat, name='chat'),
    path('checkout', views.checkout, name='checkout'),
    path('colors', views.colors, name='colors'),
    path('columns', views.columns, name='columns'),
    path('comingsoon', views.comingsoon, name='comingsoon'),
    path('contacts', views.contacts, name='contacts'),
    path('contactus', views.contactus, name='contactus'),
    path('createpasswordbasic', views.createpasswordbasic, name='createpasswordbasic'),
    path('createpasswordcover', views.createpasswordcover, name='createpasswordcover'),
    path('crmcompanies', views.crmcompanies, name='crmcompanies'),
    path('crmcontacts', views.crmcontacts, name='crmcontacts'),
    path('crmdeals', views.crmdeals, name='crmdeals'),
    path('crmleads', views.crmleads, name='crmleads'),
    path('cryptobuysell', views.cryptobuysell, name='cryptobuysell'),
    path('cryptocurrencyexchange', views.cryptocurrencyexchange, name='cryptocurrencyexchange'),
    path('cryptomarketcap', views.cryptomarketcap, name='cryptomarketcap'),
    path('cryptotransactions', views.cryptotransactions, name='cryptotransactions'),
    path('cryptowallet', views.cryptowallet, name='cryptowallet'),
    path('cssgrid', views.cssgrid, name='cssgrid'),
    path('datatables', views.datatables, name='datatables'),
    path('draggablecards', views.draggablecards, name='draggablecards'),
    path('dropdowns', views.dropdowns, name='dropdowns'),
    path('echarts', views.echarts, name='echarts'),
    path('editproducts', views.editproducts, name='editproducts'),
    path('emptypage', views.emptypage, name='emptypage'),
    path('error401', views.error401, name='error401'),
    path('error404', views.error404, name='error404'),
    path('error500', views.error500, name='error500'),
    path('faqs', views.faqs, name='faqs'),
    path('filemanager', views.filemanager, name='filemanager'),
    path('flex', views.flex, name='flex'),
    path('floatinglabels', views.floatinglabels, name='floatinglabels'),
    path('formcheckradios', views.formcheckradios, name='formcheckradios'),
    path('formcolorpickers', views.formcolorpickers, name='formcolorpickers'),
    path('formdateTimepickers', views.formdateTimepickers, name='formdateTimepickers'),
    path('formfileuploads', views.formfileuploads, name='formfileuploads'),
    path('forminputgroup', views.forminputgroup, name='forminputgroup'),
    path('forminputmasks', views.forminputmasks, name='forminputmasks'),
    path('forminputs', views.forminputs, name='forminputs'),
    path('formlayout', views.formlayout, name='formlayout'),
    path('formrange', views.formrange, name='formrange'),
    path('formselect', views.formselect, name='formselect'),
    path('formselect2', views.formselect2, name='formselect2'),
    path('formvalidation', views.formvalidation, name='formvalidation'),
    path('fullcalendar', views.fullcalendar, name='fullcalendar'),
    path('gallery', views.gallery, name='gallery'),
    path('googlemaps', views.googlemaps, name='googlemaps'),
    path('gridtables', views.gridtables, name='gridtables'),
    path('gutters', views.gutters, name='gutters'),
    path('helpers', views.helpers, name='helpers'),
    path('icons', views.icons, name='icons'),
    path('imagesfigures', views.imagesfigures, name='imagesfigures'),
    path('index1', views.index1, name='index1'),
    path('index2', views.index2, name='index2'),
    path('index3', views.index3, name='index3'),
    path('index4', views.index4, name='index4'),
    path('index5', views.index5, name='index5'),
    path('index6', views.index6, name='index6'),
    path('index7', views.index7, name='index7'),
    path('index8', views.index8, name='index8'),
    path('index9', views.index9, name='index9'),
    path('index10', views.index10, name='index10'),
    path('index11', views.index11, name='index11'),
    path('invoicecreate', views.invoicecreate, name='invoicecreate'),
    path('invoicedetails', views.invoicedetails, name='invoicedetails'),
    path('invoicelist', views.invoicelist, name='invoicelist'),
    path('jobcandidatedetails', views.jobcandidatedetails, name='jobcandidatedetails'),
    path('jobcandidatesearch', views.jobcandidatesearch, name='jobcandidatesearch'),
    path('jobcompanysearch', views.jobcompanysearch, name='jobcompanysearch'),
    path('jobdetails', views.jobdetails, name='jobdetails'),
    path('jobpost', views.jobpost, name='jobpost'),
    path('jobsearch', views.jobsearch, name='jobsearch'),
    path('jobslist', views.jobslist, name='jobslist'),
    path('landing', views.landing, name='landing'),
    path('landingjobs', views.landingjobs, name='landingjobs'),
    path('leafletmaps', views.leafletmaps, name='leafletmaps'),
    path('listgroup', views.listgroup, name='listgroup'),
    path('lockscreenbasic', views.lockscreenbasic, name='lockscreenbasic'),
    path('lockscreencover', views.lockscreencover, name='lockscreencover'),
    path('mail', views.mail, name='mail'),
    path('mailsettings', views.mailsettings, name='mailsettings'),
    path('modalscloses', views.modalscloses, name='modalscloses'),
    path('more', views.more, name='more'),
    path('navbar', views.navbar, name='navbar'),
    path('navstabs', views.navstabs, name='navstabs'),
    path('nftcreate', views.nftcreate, name='nftcreate'),
    path('nftdetails', views.nftdetails, name='nftdetails'),
    path('nftliveauction', views.nftliveauction, name='nftliveauction'),
    path('nftmarketplace', views.nftmarketplace, name='nftmarketplace'),
    path('nftwalletintegration', views.nftwalletintegration, name='nftwalletintegration'),
    path('notifications', views.notifications, name='notifications'),
    path('objectfit', views.objectfit, name='objectfit'),
    path('offcanvas', views.offcanvas, name='offcanvas'),
    path('orderdetails', views.orderdetails, name='orderdetails'),
    path('orders', views.orders, name='orders'),
    path('pagination', views.pagination, name='pagination'),
    path('placeholders', views.placeholders, name='placeholders'),
    path('popovers', views.popovers, name='popovers'),
    path('position', views.position, name='position'),
    path('pricing', views.pricing, name='pricing'),
    path('productdetails', views.productdetails, name='productdetails'),
    path('products', views.products, name='products'),
    path('productslist', views.productslist, name='productslist'),
    path('profile', views.profile, name='profile'),
    path('progress', views.progress, name='progress'),
    path('projectscreate', views.projectscreate, name='projectscreate'),
    path('projectslist', views.projectslist, name='projectslist'),
    path('projectsoverview', views.projectsoverview, name='projectsoverview'),
    path('quilleditor', views.quilleditor, name='quilleditor'),
    path('ratings', views.ratings, name='ratings'),
    path('resetpasswordbasic', views.resetpasswordbasic, name='resetpasswordbasic'),
    path('resetpasswordcover', views.resetpasswordcover, name='resetpasswordcover'),
    path('reviews', views.reviews, name='reviews'),
    path('api/sales-data/', views.sales_data, name='sales-data'),
    path('scrollspy', views.scrollspy, name='scrollspy'),
    path('signinbasic', views.signinbasic, name='signinbasic'),
    path('signincover', views.signincover, name='signincover'),
    path('signupbasic', views.signupbasic, name='signupbasic'),
    path('signupcover', views.signupcover, name='signupcover'),
    path('spinners', views.spinners, name='spinners'),
    path('sweetalerts', views.sweetalerts, name='sweetalerts'),
    path('swiperjs', views.swiperjs, name='swiperjs'),
    path('tables', views.tables, name='tables'),
    path('taskdetails', views.taskdetails, name='taskdetails'),
    path('taskkanbanboard', views.taskkanbanboard, name='taskkanbanboard'),
    path('tasklistview', views.tasklistview, name='tasklistview'),
    path('team', views.team, name='team'),
    path('termsconditions', views.termsconditions, name='termsconditions'),
    path('timeline', views.timeline, name='timeline'),
    path('toasts', views.toasts, name='toasts'),
    path('todolist', views.todolist, name='todolist'),
    path('tooltips', views.tooltips, name='tooltips'),
    path('twostepverificationbasic', views.twostepverificationbasic, name='twostepverificationbasic'),
    path('twostepverificationcover', views.twostepverificationcover, name='twostepverificationcover'),
    path('typography', views.typography, name='typography'),
    path('undermaintenance', views.undermaintenance, name='undermaintenance'),
    path('vectormaps', views.vectormaps, name='vectormaps'),
    path('widgets', views.widgets, name='widgets'),
    path('wishlist', views.wishlist, name='wishlist'),
]