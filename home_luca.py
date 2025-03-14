HOME = '''<!DOCTYPE html>
<html lang="en-US" class="js"><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8"><style data-tippy-stylesheet="">.tippy-tooltip[data-animation=fade][data-state=hidden]{opacity:0}.tippy-iOS{cursor:pointer!important;-webkit-tap-highlight-color:transparent}</style><style type="text/css">.swal-icon--error{border-color:#f27474;-webkit-animation:animateErrorIcon .5s;animation:animateErrorIcon .5s}.swal-icon--error__x-mark{position:relative;display:block;-webkit-animation:animateXMark .5s;animation:animateXMark .5s}.swal-icon--error__line{position:absolute;height:5px;width:47px;background-color:#f27474;display:block;top:37px;border-radius:2px}.swal-icon--error__line--left{-webkit-transform:rotate(45deg);transform:rotate(45deg);left:17px}.swal-icon--error__line--right{-webkit-transform:rotate(-45deg);transform:rotate(-45deg);right:16px}@-webkit-keyframes animateErrorIcon{0%{-webkit-transform:rotateX(100deg);transform:rotateX(100deg);opacity:0}to{-webkit-transform:rotateX(0deg);transform:rotateX(0deg);opacity:1}}@keyframes animateErrorIcon{0%{-webkit-transform:rotateX(100deg);transform:rotateX(100deg);opacity:0}to{-webkit-transform:rotateX(0deg);transform:rotateX(0deg);opacity:1}}@-webkit-keyframes animateXMark{0%{-webkit-transform:scale(.4);transform:scale(.4);margin-top:26px;opacity:0}50%{-webkit-transform:scale(.4);transform:scale(.4);margin-top:26px;opacity:0}80%{-webkit-transform:scale(1.15);transform:scale(1.15);margin-top:-6px}to{-webkit-transform:scale(1);transform:scale(1);margin-top:0;opacity:1}}@keyframes animateXMark{0%{-webkit-transform:scale(.4);transform:scale(.4);margin-top:26px;opacity:0}50%{-webkit-transform:scale(.4);transform:scale(.4);margin-top:26px;opacity:0}80%{-webkit-transform:scale(1.15);transform:scale(1.15);margin-top:-6px}to{-webkit-transform:scale(1);transform:scale(1);margin-top:0;opacity:1}}.swal-icon--warning{border-color:#f8bb86;-webkit-animation:pulseWarning .75s infinite alternate;animation:pulseWarning .75s infinite alternate}.swal-icon--warning__body{width:5px;height:47px;top:10px;border-radius:2px;margin-left:-2px}.swal-icon--warning__body,.swal-icon--warning__dot{position:absolute;left:50%;background-color:#f8bb86}.swal-icon--warning__dot{width:7px;height:7px;border-radius:50%;margin-left:-4px;bottom:-11px}@-webkit-keyframes pulseWarning{0%{border-color:#f8d486}to{border-color:#f8bb86}}@keyframes pulseWarning{0%{border-color:#f8d486}to{border-color:#f8bb86}}.swal-icon--success{border-color:#a5dc86}.swal-icon--success:after,.swal-icon--success:before{content:"";border-radius:50%;position:absolute;width:60px;height:120px;background:#fff;-webkit-transform:rotate(45deg);transform:rotate(45deg)}.swal-icon--success:before{border-radius:120px 0 0 120px;top:-7px;left:-33px;-webkit-transform:rotate(-45deg);transform:rotate(-45deg);-webkit-transform-origin:60px 60px;transform-origin:60px 60px}.swal-icon--success:after{border-radius:0 120px 120px 0;top:-11px;left:30px;-webkit-transform:rotate(-45deg);transform:rotate(-45deg);-webkit-transform-origin:0 60px;transform-origin:0 60px;-webkit-animation:rotatePlaceholder 4.25s ease-in;animation:rotatePlaceholder 4.25s ease-in}.swal-icon--success__ring{width:80px;height:80px;border:4px solid hsla(98,55%,69%,.2);border-radius:50%;box-sizing:content-box;position:absolute;left:-4px;top:-4px;z-index:2}.swal-icon--success__hide-corners{width:5px;height:90px;background-color:#fff;padding:1px;position:absolute;left:28px;top:8px;z-index:1;-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}.swal-icon--success__line{height:5px;background-color:#a5dc86;display:block;border-radius:2px;position:absolute;z-index:2}.swal-icon--success__line--tip{width:25px;left:14px;top:46px;-webkit-transform:rotate(45deg);transform:rotate(45deg);-webkit-animation:animateSuccessTip .75s;animation:animateSuccessTip .75s}.swal-icon--success__line--long{width:47px;right:8px;top:38px;-webkit-transform:rotate(-45deg);transform:rotate(-45deg);-webkit-animation:animateSuccessLong .75s;animation:animateSuccessLong .75s}@-webkit-keyframes rotatePlaceholder{0%{-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}5%{-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}12%{-webkit-transform:rotate(-405deg);transform:rotate(-405deg)}to{-webkit-transform:rotate(-405deg);transform:rotate(-405deg)}}@keyframes rotatePlaceholder{0%{-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}5%{-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}12%{-webkit-transform:rotate(-405deg);transform:rotate(-405deg)}to{-webkit-transform:rotate(-405deg);transform:rotate(-405deg)}}@-webkit-keyframes animateSuccessTip{0%{width:0;left:1px;top:19px}54%{width:0;left:1px;top:19px}70%{width:50px;left:-8px;top:37px}84%{width:17px;left:21px;top:48px}to{width:25px;left:14px;top:45px}}@keyframes animateSuccessTip{0%{width:0;left:1px;top:19px}54%{width:0;left:1px;top:19px}70%{width:50px;left:-8px;top:37px}84%{width:17px;left:21px;top:48px}to{width:25px;left:14px;top:45px}}@-webkit-keyframes animateSuccessLong{0%{width:0;right:46px;top:54px}65%{width:0;right:46px;top:54px}84%{width:55px;right:0;top:35px}to{width:47px;right:8px;top:38px}}@keyframes animateSuccessLong{0%{width:0;right:46px;top:54px}65%{width:0;right:46px;top:54px}84%{width:55px;right:0;top:35px}to{width:47px;right:8px;top:38px}}.swal-icon--info{border-color:#c9dae1}.swal-icon--info:before{width:5px;height:29px;bottom:17px;border-radius:2px;margin-left:-2px}.swal-icon--info:after,.swal-icon--info:before{content:"";position:absolute;left:50%;background-color:#c9dae1}.swal-icon--info:after{width:7px;height:7px;border-radius:50%;margin-left:-3px;top:19px}.swal-icon{width:80px;height:80px;border-width:4px;border-style:solid;border-radius:50%;padding:0;position:relative;box-sizing:content-box;margin:20px auto}.swal-icon:first-child{margin-top:32px}.swal-icon--custom{width:auto;height:auto;max-width:100%;border:none;border-radius:0}.swal-icon img{max-width:100%;max-height:100%}.swal-title{color:rgba(0,0,0,.65);font-weight:600;text-transform:none;position:relative;display:block;padding:13px 16px;font-size:27px;line-height:normal;text-align:center;margin-bottom:0}.swal-title:first-child{margin-top:26px}.swal-title:not(:first-child){padding-bottom:0}.swal-title:not(:last-child){margin-bottom:13px}.swal-text{font-size:16px;position:relative;float:none;line-height:normal;vertical-align:top;text-align:left;display:inline-block;margin:0;padding:0 10px;font-weight:400;color:rgba(0,0,0,.64);max-width:calc(100% - 20px);overflow-wrap:break-word;box-sizing:border-box}.swal-text:first-child{margin-top:45px}.swal-text:last-child{margin-bottom:45px}.swal-footer{text-align:right;padding-top:13px;margin-top:13px;padding:13px 16px;border-radius:inherit;border-top-left-radius:0;border-top-right-radius:0}.swal-button-container{margin:5px;display:inline-block;position:relative}.swal-button{background-color:#7cd1f9;color:#fff;border:none;box-shadow:none;border-radius:5px;font-weight:600;font-size:14px;padding:10px 24px;margin:0;cursor:pointer}.swal-button:not([disabled]):hover{background-color:#78cbf2}.swal-button:active{background-color:#70bce0}.swal-button:focus{outline:none;box-shadow:0 0 0 1px #fff,0 0 0 3px rgba(43,114,165,.29)}.swal-button[disabled]{opacity:.5;cursor:default}.swal-button::-moz-focus-inner{border:0}.swal-button--cancel{color:#555;background-color:#efefef}.swal-button--cancel:not([disabled]):hover{background-color:#e8e8e8}.swal-button--cancel:active{background-color:#d7d7d7}.swal-button--cancel:focus{box-shadow:0 0 0 1px #fff,0 0 0 3px rgba(116,136,150,.29)}.swal-button--danger{background-color:#e64942}.swal-button--danger:not([disabled]):hover{background-color:#df4740}.swal-button--danger:active{background-color:#cf423b}.swal-button--danger:focus{box-shadow:0 0 0 1px #fff,0 0 0 3px rgba(165,43,43,.29)}.swal-content{padding:0 20px;margin-top:20px;font-size:medium}.swal-content:last-child{margin-bottom:20px}.swal-content__input,.swal-content__textarea{-webkit-appearance:none;background-color:#fff;border:none;font-size:14px;display:block;box-sizing:border-box;width:100%;border:1px solid rgba(0,0,0,.14);padding:10px 13px;border-radius:2px;transition:border-color .2s}.swal-content__input:focus,.swal-content__textarea:focus{outline:none;border-color:#6db8ff}.swal-content__textarea{resize:vertical}.swal-button--loading{color:transparent}.swal-button--loading~.swal-button__loader{opacity:1}.swal-button__loader{position:absolute;height:auto;width:43px;z-index:2;left:50%;top:50%;-webkit-transform:translateX(-50%) translateY(-50%);transform:translateX(-50%) translateY(-50%);text-align:center;pointer-events:none;opacity:0}.swal-button__loader div{display:inline-block;float:none;vertical-align:baseline;width:9px;height:9px;padding:0;border:none;margin:2px;opacity:.4;border-radius:7px;background-color:hsla(0,0%,100%,.9);transition:background .2s;-webkit-animation:swal-loading-anim 1s infinite;animation:swal-loading-anim 1s infinite}.swal-button__loader div:nth-child(3n+2){-webkit-animation-delay:.15s;animation-delay:.15s}.swal-button__loader div:nth-child(3n+3){-webkit-animation-delay:.3s;animation-delay:.3s}@-webkit-keyframes swal-loading-anim{0%{opacity:.4}20%{opacity:.4}50%{opacity:1}to{opacity:.4}}@keyframes swal-loading-anim{0%{opacity:.4}20%{opacity:.4}50%{opacity:1}to{opacity:.4}}.swal-overlay{position:fixed;top:0;bottom:0;left:0;right:0;text-align:center;font-size:0;overflow-y:auto;background-color:rgba(0,0,0,.4);z-index:10000;pointer-events:none;opacity:0;transition:opacity .3s}.swal-overlay:before{content:" ";display:inline-block;vertical-align:middle;height:100%}.swal-overlay--show-modal{opacity:1;pointer-events:auto}.swal-overlay--show-modal .swal-modal{opacity:1;pointer-events:auto;box-sizing:border-box;-webkit-animation:showSweetAlert .3s;animation:showSweetAlert .3s;will-change:transform}.swal-modal{width:478px;opacity:0;pointer-events:none;background-color:#fff;text-align:center;border-radius:5px;position:static;margin:20px auto;display:inline-block;vertical-align:middle;-webkit-transform:scale(1);transform:scale(1);-webkit-transform-origin:50% 50%;transform-origin:50% 50%;z-index:10001;transition:opacity .2s,-webkit-transform .3s;transition:transform .3s,opacity .2s;transition:transform .3s,opacity .2s,-webkit-transform .3s}@media (max-width:500px){.swal-modal{width:calc(100% - 20px)}}@-webkit-keyframes showSweetAlert{0%{-webkit-transform:scale(1);transform:scale(1)}1%{-webkit-transform:scale(.5);transform:scale(.5)}45%{-webkit-transform:scale(1.05);transform:scale(1.05)}80%{-webkit-transform:scale(.95);transform:scale(.95)}to{-webkit-transform:scale(1);transform:scale(1)}}@keyframes showSweetAlert{0%{-webkit-transform:scale(1);transform:scale(1)}1%{-webkit-transform:scale(.5);transform:scale(.5)}45%{-webkit-transform:scale(1.05);transform:scale(1.05)}80%{-webkit-transform:scale(.95);transform:scale(.95)}to{-webkit-transform:scale(1);transform:scale(1)}}</style>
	<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<link rel="pingback" href="https://www.empowersemi.com/xmlrpc.php">

	<script src="Technology%20_%20Empower%20Semiconductor_files/lftracker_v1_Xz1A5d7Ow0wdP3k2.js" async=""></script><script type="text/javascript" async="" src="Technology%20_%20Empower%20Semiconductor_files/js_002"></script><script type="text/javascript" async="" defer="defer" src="Technology%20_%20Empower%20Semiconductor_files/analytics.js"></script><script async="" src="Technology%20_%20Empower%20Semiconductor_files/gtm.js"></script><script type="text/javascript">
		document.documentElement.className = 'js';
	</script>
	
	<link media="all" href="Technology%20_%20Empower%20Semiconductor_files/autoptimize_871830a8d10a21d22446e8ff60b4c7de.css" rel="stylesheet"><title>Technology | Empower Semiconductor</title>
<link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin=""><meta name="robots" content="max-image-preview:large">
<link rel="alternate" href="https://www.empowersemi.com/technology/" hreflang="en">
<link rel="alternate" href="https://www.empowersemi.com/zh/technology-cn-3/" hreflang="zh">

            <script data-no-defer="1" data-ezscrex="false" data-cfasync="false" data-pagespeed-no-defer="" data-cookieconsent="ignore">
                var ctPublicFunctions = {"_ajax_nonce":"e52fc10605","_rest_nonce":"6dc0230fcc","_ajax_url":"\/wp-admin\/admin-ajax.php","_rest_url":"https:\/\/www.empowersemi.com\/wp-json\/","data__cookies_type":"native","data__ajax_type":"rest","data__bot_detector_enabled":"0","data__frontend_data_log_enabled":1,"cookiePrefix":"","wprocket_detected":false,"host_url":"www.empowersemi.com","text__ee_click_to_select":"Click to select the whole data","text__ee_original_email":"The original one is","text__ee_got_it":"Got it","text__ee_blocked":"Blocked","text__ee_cannot_connect":"Cannot connect","text__ee_cannot_decode":"Can not decode email. Unknown reason","text__ee_email_decoder":"CleanTalk email decoder","text__ee_wait_for_decoding":"The magic is on the way, please wait for a few seconds!","text__ee_decoding_process":"Decoding the contact data, let us a few seconds to finish."}
            </script>
        
            <script data-no-defer="1" data-ezscrex="false" data-cfasync="false" data-pagespeed-no-defer="" data-cookieconsent="ignore">
                var ctPublic = {"_ajax_nonce":"e52fc10605","settings__forms__check_internal":"0","settings__forms__check_external":"1","settings__forms__force_protection":0,"settings__forms__search_test":"1","settings__data__bot_detector_enabled":"0","settings__sfw__anti_crawler":0,"blog_home":"https:\/\/www.empowersemi.com\/","pixel__setting":"0","pixel__enabled":false,"pixel__url":null,"data__email_check_before_post":"1","data__email_check_exist_post":0,"data__cookies_type":"native","data__key_is_ok":true,"data__visible_fields_required":true,"wl_brandname":"Anti-Spam by CleanTalk","wl_brandname_short":"CleanTalk","ct_checkjs_key":"626ea28402e4748156a7af6c3e215f58a61b9847d18bce15c4557106ea61cdd1","emailEncoderPassKey":"a44517a1de9834ea08fef33b71a2c60b","bot_detector_forms_excluded":"W10=","advancedCacheExists":false,"varnishCacheExists":false,"wc_ajax_add_to_cart":false}
            </script>
        <link rel="dns-prefetch" href="https://unpkg.com/">
<link rel="alternate" type="application/rss+xml" title="Empower Semiconductor » Feed" href="https://www.empowersemi.com/feed/">
<link rel="alternate" type="application/rss+xml" title="Empower Semiconductor » Comments Feed" href="https://www.empowersemi.com/comments/feed/">
<meta content="Divi v.4.27.4" name="generator">






























<link rel="stylesheet" id="csshero-main-stylesheet-css" href="Technology%20_%20Empower%20Semiconductor_files/autoptimize_single_41cb65c829c80d0d85875239a3bab7e7.css" type="text/css" media="all">



				<script>
				var divimegapro_singleton = [];
				divimegapro_singleton['header'] = false;
				divimegapro_singleton['content'] = false;
				divimegapro_singleton['footer'] = false;
				var divimegapro_singleton_enabled = ( divimegapro_singleton['header'] || divimegapro_singleton['content'] || divimegapro_singleton['footer'] ) ? true : false;
				</script>
				
				<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/jquery.min.js" id="jquery-core-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/jquery-migrate.min.js" id="jquery-migrate-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/sweetalert.min.js" id="sweetalert-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/copy.js" id="copyjs-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/apbct-public-bundle_ext-protection.min.js" id="ct_public_functions-external_forms-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/wpdm.min.js" id="wpdm-frontend-js-js"></script>
<script type="text/javascript" id="wpdm-frontjs-js-extra">
/* <![CDATA[ */
var wpdm_url = {"home":"https:\/\/www.empowersemi.com\/","site":"https:\/\/www.empowersemi.com\/","ajax":"https:\/\/www.empowersemi.com\/wp-admin\/admin-ajax.php"};
var wpdm_js = {"spinner":"<i class=\"wpdm-icon wpdm-sun wpdm-spin\"><\/i>","client_id":"4159b173dfb6f46f4bd7f5c93230872e"};
var wpdm_strings = {"pass_var":"Password Verified!","pass_var_q":"Please click following button to start download.","start_dl":"Start Download"};
/* ]]> */
</script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/front.min.js" id="wpdm-frontjs-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/popper-1.16.1.min.js" id="DiviMegaPro-popper-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/tippy-5.2.1.min.js" id="DiviMegaPro-tippy-js"></script>
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://www.empowersemi.com/xmlrpc.php?rsd">
<meta name="generator" content="WordPress 6.7.2">
<link rel="canonical" href="https://www.empowersemi.com/technology/">
<link rel="shortlink" href="https://www.empowersemi.com/?p=25190">
<link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://www.empowersemi.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.empowersemi.com%2Ftechnology%2F">
<link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://www.empowersemi.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.empowersemi.com%2Ftechnology%2F&amp;format=xml">
	<script data-name="dbdb-head-js">
	 
	</script>

        

    
    
    
<link rel="apple-touch-icon" sizes="180x180" href="https://www.empowersemi.com/wp-content/uploads/fbrfg/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="https://www.empowersemi.com/wp-content/uploads/fbrfg/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="https://www.empowersemi.com/wp-content/uploads/fbrfg/favicon-16x16.png">
<link rel="manifest" href="https://www.empowersemi.com/wp-content/uploads/fbrfg/site.webmanifest">
<link rel="mask-icon" href="https://www.empowersemi.com/wp-content/uploads/fbrfg/safari-pinned-tab.svg" color="#5bbad5">
<link rel="shortcut icon" href="https://www.empowersemi.com/wp-content/uploads/fbrfg/favicon.ico">
<meta name="msapplication-TileColor" content="#da532c">
<meta name="msapplication-config" content="/wp-content/uploads/fbrfg/browserconfig.xml">
<meta name="theme-color" content="#ffffff">				<script>
				  // Define dataLayer and the gtag function.
				  window.dataLayer = window.dataLayer || [];
				  function gtag(){dataLayer.push(arguments);}

				  // Set default consent to 'denied' as a placeholder
				  // Determine actual values based on your own requirements
				  gtag('consent', 'default', {
				    'ad_storage': 'denied',
				    'ad_user_data': 'denied',
				    'ad_personalization': 'denied',
				    'analytics_storage': 'denied',
				    'personalization_storage': 'denied',
						'security_storage': 'denied',
						'functionality_storage': 'denied',
						'wait_for_update': '2000'
				  });
				</script>

				<!-- Google Tag Manager -->
				<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
				new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
				j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
				'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
				})(window,document,'script','dataLayer','GTM-TWLTKCL6');</script>
				<!-- End Google Tag Manager -->
					<script>
			document.documentElement.className = document.documentElement.className.replace('no-js', 'js');
		</script>
				
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">		<script type="text/javascript">
		var ajax_url = 'https://www.empowersemi.com/wp-admin/admin-ajax.php';
		</script>
		<meta name="generator" content="Powered by Slider Revolution 6.7.29 - responsive, Mobile-Friendly Slider Plugin for WordPress with comfortable drag and drop interface.">
<script>function setREVStartSize(e){
			//window.requestAnimationFrame(function() {
				window.RSIW = window.RSIW===undefined ? window.innerWidth : window.RSIW;
				window.RSIH = window.RSIH===undefined ? window.innerHeight : window.RSIH;
				try {
					var pw = document.getElementById(e.c).parentNode.offsetWidth,
						newh;
					pw = pw===0 || isNaN(pw) || (e.l=="fullwidth" || e.layout=="fullwidth") ? window.RSIW : pw;
					e.tabw = e.tabw===undefined ? 0 : parseInt(e.tabw);
					e.thumbw = e.thumbw===undefined ? 0 : parseInt(e.thumbw);
					e.tabh = e.tabh===undefined ? 0 : parseInt(e.tabh);
					e.thumbh = e.thumbh===undefined ? 0 : parseInt(e.thumbh);
					e.tabhide = e.tabhide===undefined ? 0 : parseInt(e.tabhide);
					e.thumbhide = e.thumbhide===undefined ? 0 : parseInt(e.thumbhide);
					e.mh = e.mh===undefined || e.mh=="" || e.mh==="auto" ? 0 : parseInt(e.mh,0);
					if(e.layout==="fullscreen" || e.l==="fullscreen")
						newh = Math.max(e.mh,window.RSIH);
					else{
						e.gw = Array.isArray(e.gw) ? e.gw : [e.gw];
						for (var i in e.rl) if (e.gw[i]===undefined || e.gw[i]===0) e.gw[i] = e.gw[i-1];
						e.gh = e.el===undefined || e.el==="" || (Array.isArray(e.el) && e.el.length==0)? e.gh : e.el;
						e.gh = Array.isArray(e.gh) ? e.gh : [e.gh];
						for (var i in e.rl) if (e.gh[i]===undefined || e.gh[i]===0) e.gh[i] = e.gh[i-1];
											
						var nl = new Array(e.rl.length),
							ix = 0,
							sl;
						e.tabw = e.tabhide>=pw ? 0 : e.tabw;
						e.thumbw = e.thumbhide>=pw ? 0 : e.thumbw;
						e.tabh = e.tabhide>=pw ? 0 : e.tabh;
						e.thumbh = e.thumbhide>=pw ? 0 : e.thumbh;
						for (var i in e.rl) nl[i] = e.rl[i]<window.RSIW ? 0 : e.rl[i];
						sl = nl[0];
						for (var i in nl) if (sl>nl[i] && nl[i]>0) { sl = nl[i]; ix=i;}
						var m = pw>(e.gw[ix]+e.tabw+e.thumbw) ? 1 : (pw-(e.tabw+e.thumbw)) / (e.gw[ix]);
						newh =  (e.gh[ix] * m) + (e.tabh + e.thumbh);
					}
					var el = document.getElementById(e.c);
					if (el!==null && el) el.style.height = newh+"px";
					el = document.getElementById(e.c+"_wrapper");
					if (el!==null && el) {
						el.style.height = newh+"px";
						el.style.display = "block";
					}
				} catch(e){
					console.log("Failure at Presize of Slider:" + e)
				}
			//});
		  };</script>
<meta name="generator" content="WordPress Download Manager 3.3.09">
                
                
        <style id="fit-vids-style">.fluid-width-video-wrapper{width:100%;position:relative;padding:0;}.fluid-width-video-wrapper iframe,.fluid-width-video-wrapper object,.fluid-width-video-wrapper embed {position:absolute;top:0;left:0;width:100%;height:100%;}</style><style id="divi-mega-pro-styles"></style><style id="divi-mega-pro-styles"></style><script data-gdpr=""> (function(ss,ex){ window.ldfdr=window.ldfdr||function(){(ldfdr._q=ldfdr._q||[]).push([].slice.call(arguments));}; (function(d,s){ fs=d.getElementsByTagName(s)[0]; function ce(src){ var cs=d.createElement(s); cs.src=src; cs.async=1; fs.parentNode.insertBefore(cs,fs); }; ce('https://sc.lfeeder.com/lftracker_v1_'+ss+(ex?'_'+ex:'')+'.js'); })(document,'script'); })('Xz1A5d7Ow0wdP3k2'); </script>				<!-- Google tag (gtag.js) - Google Analytics 4 -->
				<script data-gdpr="" src="Technology%20_%20Empower%20Semiconductor_files/js" data-type="gdpr-integration"></script>
				<script data-gdpr="" data-type="gdpr-integration">
				  window.dataLayer = window.dataLayer || [];
				  function gtag(){dataLayer.push(arguments);}
				  gtag('js', new Date());

				  gtag('config', 'G-YSWE9FLBZ4');
				</script>
								<script data-gdpr="">
					gtag('consent', 'update', {
			      'ad_storage': 'granted',
				    'ad_user_data': 'granted',
				    'ad_personalization': 'granted',
				    'analytics_storage': 'granted',
				    'personalization_storage': 'granted',
						'security_storage': 'granted',
						'functionality_storage': 'granted',
			    });

			    dataLayer.push({
					 'event': 'cookie_consent_update'
					});
				</script>	
				</head>
<body data-rsssl="1" class="page-template-default page page-id-25190 et-tb-has-template et-tb-has-header et-tb-has-footer dbdb_divi_2_4_up et_pb_button_helper_class et_cover_background et_pb_gutter windows et_pb_gutters3 et_pb_pagebuilder_layout et_no_sidebar et_divi_theme et-db divimegapro-active gecko gdpr-infobar-visible">
	<script type="text/javascript">var overlays_with_css_trigger = {};</script><script type="text/javascript">var overlays_with_automatic_trigger = {'219806': '{"at_type":"0","at_value":"0","at_onceperload":"0"}',};</script>				<script>
				var divimegapro_singleton = [];
				divimegapro_singleton['header'] = false;
				divimegapro_singleton['content'] = false;
				divimegapro_singleton['footer'] = false;
				var divimegapro_singleton_enabled = ( divimegapro_singleton['header'] || divimegapro_singleton['content'] || divimegapro_singleton['footer'] ) ? true : false;
				</script>
				
									<script>
					var ajaxurl = "https://www.empowersemi.com/wp-admin/admin-ajax.php"
					, diviLifeisMobileDevice = "false"
					, diviLifeisTabletDevice = "false";
					</script>
					<div class="et-l et-l--post">
			<div class="et_builder_inner_content et_pb_gutters3">
		

		</div>
	</div>
	<div id="page-container"><div class="divimegapro-wrapper">
<div id="divimegapro-container-263745" class="divimegapro-container" data-animation="shift-away" data-bgcolor="" data-fontcolor="" data-placement="left" data-margintopbottom="" data-megaprowidth="custom" data-megaprowidthcustom="450px" data-megaprofixedheight="" data-triggertype="hover" data-exittype="hover" data-exitdelay="" data-enable_arrow="0" data-arrowfeature_type="sharp" data-dmp_cssposition="absolute" data-dmp_enablecenterhorizontal="0" style="display:none">
<div id="divimegapro-263745" class="divimegapro divimegapro-flexheight">
<div class="divimegapro-pre-body">
<div class="divimegapro-body"><div class="et_pb_with_border et_pb_section et_pb_section_0 et_pb_with_background et_section_regular">
				
				
				
				
				
				
				<div class="et_pb_row et_pb_row_0">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_0  et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				
				
				<div class="et_pb_module et_pb_text et_pb_text_0  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><p>High-speed designs use digital 
components with very fast edge rates in their output signals which can 
be subjected to significant distortion and degradation creating high 
bit-error-rates and lower data throughput.&nbsp; Insertion and 
reflection losses, crosstalk and impedance mismatch, are all factors, 
amongst others, influencing the integrity of a transmitted signal.</p>
<p>Empower’s E-CAP silicon capacitors provide wide bandwidth low 
impedance highly stable decoupling capacitors capable of being placed 
close and even integrated into an SoC substrate.</p></div>
			</div>
			</div>
				
				
				
				
			</div>
				
				
			</div></div>
</div>
<div class="divimegapro-close-container dmp_enabledesktop"><button type="button" class="divimegapro-close divimegapro-customclose-btn-263745" data-dmpid="263745" title="Close dialog" aria-disabled="true"><span class="dmm-custom-btn">×</span></button></div>
</div>
</div>
<div id="divimegapro-container-263741" class="divimegapro-container" data-animation="shift-away" data-bgcolor="" data-fontcolor="" data-placement="left" data-margintopbottom="" data-megaprowidth="custom" data-megaprowidthcustom="450px" data-megaprofixedheight="" data-triggertype="hover" data-exittype="hover" data-exitdelay="" data-enable_arrow="0" data-arrowfeature_type="sharp" data-dmp_cssposition="absolute" data-dmp_enablecenterhorizontal="0" style="display:none">
<div id="divimegapro-263741" class="divimegapro divimegapro-flexheight">
<div class="divimegapro-pre-body">
<div class="divimegapro-body"><div class="et_pb_with_border et_pb_section et_pb_section_1 et_pb_with_background et_section_regular">
				
				
				
				
				
				
				<div class="et_pb_row et_pb_row_1">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_1  et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				
				
				<div class="et_pb_module et_pb_text et_pb_text_1  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><p>Empower Semiconductor is developing
 power management solutions enabling full unrestricted speed and 
performance of the latest xPUs.</p>
<ul>
<li>High power density</li>
<li>High bandwidth conversion</li>
<li>Low power distribution losses</li>
<li>Vertical Power</li>
</ul>
<p>The ability to process data and perform complex calculations at high 
speeds has been intensified in recent years by leaps in technologies 
such as artificial intelligence, 3-D imaging and autonomous driving. 
These technologies have exacerbated the need for faster and more complex
 processors and architectures.</p></div>
			</div>
			</div>
				
				
				
				
			</div>
				
				
			</div></div>
</div>
<div class="divimegapro-close-container dmp_enabledesktop"><button type="button" class="divimegapro-close divimegapro-customclose-btn-263741" data-dmpid="263741" title="Close dialog" aria-disabled="true"><span class="dmm-custom-btn">×</span></button></div>
</div>
</div>
<div id="divimegapro-container-263736" class="divimegapro-container" data-animation="fade" data-bgcolor="" data-fontcolor="" data-placement="right" data-margintopbottom="" data-megaprowidth="custom" data-megaprowidthcustom="450px" data-megaprofixedheight="" data-triggertype="hover" data-exittype="hover" data-exitdelay="" data-enable_arrow="0" data-arrowfeature_type="sharp" data-dmp_cssposition="absolute" data-dmp_enablecenterhorizontal="0" style="display:none">
<div id="divimegapro-263736" class="divimegapro divimegapro-flexheight">
<div class="divimegapro-pre-body">
<div class="divimegapro-body"><div class="et_pb_with_border et_pb_section et_pb_section_2 et_pb_with_background et_section_regular">
				
				
				
				
				
				
				<div class="et_pb_row et_pb_row_2">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_2  et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				
				
				<div class="et_pb_module et_pb_text et_pb_text_2  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><p>Equipment designed to operate 
within a high magnetic field environment can experience power failures 
or abnormal operating conditions due to the force the magnetic field 
imposes on ferromagnetic material-based electronics.</p>
<p>Moreover, magnetic resonance imaging (MRI) devices can record false 
or distorted images due to the inferences from such electronics. 
Empower’s IVRs regulators use non-ferromagnetic air-core inductors ideal
 for operating in harsh magnetic environments.</p></div>
			</div>
			</div>
				
				
				
				
			</div>
				
				
			</div></div>
</div>
<div class="divimegapro-close-container dmp_enabledesktop"><button type="button" class="divimegapro-close divimegapro-customclose-btn-263736" data-dmpid="263736" title="Close dialog" aria-disabled="true"><span class="dmm-custom-btn">×</span></button></div>
</div>
</div>
<div id="divimegapro-container-263695" class="divimegapro-container" data-animation="shift-away" data-bgcolor="" data-fontcolor="" data-placement="left" data-margintopbottom="" data-megaprowidth="custom" data-megaprowidthcustom="450px" data-megaprofixedheight="" data-triggertype="hover" data-exittype="hover" data-exitdelay="" data-enable_arrow="0" data-arrowfeature_type="sharp" data-dmp_cssposition="absolute" data-dmp_enablecenterhorizontal="0" style="display:none">
<div id="divimegapro-263695" class="divimegapro divimegapro-flexheight">
<div class="divimegapro-pre-body">
<div class="divimegapro-body"><div class="et_pb_with_border et_pb_section et_pb_section_3 et_pb_with_background et_section_regular">
				
				
				
				
				
				
				<div class="et_pb_row et_pb_row_3">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_3  et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				
				
				<div class="et_pb_module et_pb_text et_pb_text_3  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><p>Data being communicated and 
processed around the globe is rapidly growing, driving the need for a 
new generation of faster data processing components and elements in data
 centers and datacom equipment.</p>
<p>Empower Semiconductor offers novel fully integrated power management 
solutions that both increase performance and solve the power density 
challenge of space-constrained data-intensive applications.</p>
<p><a href="https://www.empowersemi.com/data-centers/">Click for more</a></p></div>
			</div>
			</div>
				
				
				
				
			</div>
				
				
			</div></div>
</div>
<div class="divimegapro-close-container dmp_enabledesktop"><button type="button" class="divimegapro-close divimegapro-customclose-btn-263695" data-dmpid="263695" title="Close dialog" aria-disabled="true"><span class="dmm-custom-btn">×</span></button></div>
</div>
</div>
<div id="divimegapro-container-263673" class="divimegapro-container" data-animation="shift-away" data-bgcolor="" data-fontcolor="" data-placement="right" data-margintopbottom="" data-megaprowidth="custom" data-megaprowidthcustom="450px" data-megaprofixedheight="" data-triggertype="hover" data-exittype="hover" data-exitdelay="" data-enable_arrow="0" data-arrowfeature_type="sharp" data-dmp_cssposition="absolute" data-dmp_enablecenterhorizontal="0" style="display:none">
<div id="divimegapro-263673" class="divimegapro divimegapro-flexheight">
<div class="divimegapro-pre-body">
<div class="divimegapro-body"><div class="et_pb_with_border et_pb_section et_pb_section_4 et_pb_with_background et_section_regular">
				
				
				
				
				
				
				<div class="et_pb_row et_pb_row_4">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_4  et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				
				
				<div class="et_pb_module et_pb_text et_pb_text_4  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><span style="font-size:14px;">System-
on-Modules (SOMs) and Computer-on-Modules (CoMs) provide all components 
of an embedded processing system (processors, communication interfaces, 
memory blocks, power management, etc.) on a single production-ready 
printed circuit board (PCB). This modular approach makes them ideal for 
embedding into a variety of end systems and applications.<p></p>
<p>Empower’s IVRs provide high-density configurable multi-rails regulators enabling rapid and flexible prototyping.</p></span></div>
			</div>
			</div>
				
				
				
				
			</div>
				
				
			</div></div>
</div>
<div class="divimegapro-close-container dmp_enabledesktop"><button type="button" class="divimegapro-close divimegapro-customclose-btn-263673" data-dmpid="263673" title="Close dialog" aria-disabled="true"><span class="dmm-custom-btn">×</span></button></div>
</div>
</div>
<div id="divimegapro-container-263620" class="divimegapro-container" data-animation="shift-away" data-bgcolor="" data-fontcolor="" data-placement="right" data-margintopbottom="" data-megaprowidth="custom" data-megaprowidthcustom="450px" data-megaprofixedheight="" data-triggertype="hover" data-exittype="hover" data-exitdelay="" data-enable_arrow="0" data-arrowfeature_type="sharp" data-dmp_cssposition="absolute" data-dmp_enablecenterhorizontal="0" style="display:none">
<div id="divimegapro-263620" class="divimegapro divimegapro-flexheight">
<div class="divimegapro-pre-body">
<div class="divimegapro-body"><div class="et_pb_with_border et_pb_section et_pb_section_5 et_pb_with_background et_section_regular">
				
				
				
				
				
				
				<div class="et_pb_row et_pb_row_5">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_5  et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				
				
				<div class="et_pb_module et_pb_text et_pb_text_5  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><p>Chiplet architectures are rapidly 
gaining popularity over monolithic designs in developing complex SoCs. 
While providing increased performance, design flexibility and 
upgradability, they do, however, require more complex power management 
and PCB routing.</p>
<p>Empower’s IVRs can be integrated as an additional chiplet into an SoC
 increasing the power delivery efficiency and simplifying PCB routing.</p></div>
			</div>
			</div>
				
				
				
				
			</div>
				
				
			</div></div>
</div>
<div class="divimegapro-close-container dmp_enabledesktop"><button type="button" class="divimegapro-close divimegapro-customclose-btn-263620" data-dmpid="263620" title="Close dialog" aria-disabled="true"><span class="dmm-custom-btn">×</span></button></div>
</div>
</div>
</div>
<div id="et-boc" class="et-boc">
			
		<header class="et-l et-l--header">
			<div class="et_builder_inner_content et_pb_gutters3"><div id="header-desktop-row" class="et_pb_section et_pb_section_0_tb_header et_section_regular et_pb_section--with-menu">
				
				
				
				
				
				
				<div class="et_pb_row et_pb_row_0_tb_header et_pb_gutters1 et_pb_row--with-menu et_pb_row_1-4_3-4" style="z-index: 3;">
				<div class="et_pb_column et_pb_column_1_4 et_pb_column_0_tb_header  et_pb_css_mix_blend_mode_passthrough" id="col-logo">
				
				
				
				
				<div class="et_pb_module et_pb_image et_pb_image_0_tb_header">
				
				
				
				
				<a href="https://www.empowersemi.com/"><span class="et_pb_image_wrap "><img decoding="async" data-src="https://www.empowersemi.com/wp-content/uploads/2025/03/empower_logo.svg" alt="Empower Semiconductor" title="empower_logo" class="wp-image-265093 lazyloaded" src="Technology%20_%20Empower%20Semiconductor_files/empower_logo.svg"></span></a>
			</div>
			</div><div class="et_pb_column et_pb_column_3_4 et_pb_column_1_tb_header  et_pb_css_mix_blend_mode_passthrough et-last-child et_pb_column--with-menu" id="col-menu">
				
				
				
				
				<div class="et_pb_module et_pb_menu et_pb_menu_0_tb_header et_pb_bg_layout_light  et_pb_text_align_left et_dropdown_animation_fade et_pb_menu--without-logo et_pb_menu--style-centered db_title_off db_title_use_link_off db_tagline_off db_tagline_below_title_off db_title_and_tagline_valign_top db_title_and_tagline_below_logo_off">
					
					
					
					
					<div class="et_pb_menu_inner_container clearfix">
						
						<div class="et_pb_menu__wrap">
							<div class="et_pb_menu__menu">
								<nav class="et-menu-nav"><ul id="menu-main-menu" class="et-menu nav"><li class="et_pb_menu_page_id-229928 menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-229928"><a href="#">Products</a>
<ul class="sub-menu">
	<li class="et_pb_menu_page_id-256390 menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-256390"><a href="https://www.empowersemi.com/integrated-voltage-regulators-ivr/">Power Conversion</a>
	<ul class="sub-menu">
		<li class="et_pb_menu_page_id-256357 menu-item menu-item-type-post_type menu-item-object-page menu-item-256392"><a href="https://www.empowersemi.com/3-3v-integrated-voltage-regulators-ivr/">3.3V Integrated Voltage Regulators (IVR)</a></li>
		<li class="et_pb_menu_page_id-256362 menu-item menu-item-type-post_type menu-item-object-page menu-item-256391"><a href="https://www.empowersemi.com/1-8v-integrated-voltage-regulators-ivr/">1.8V Integrated Voltage Regulators (IVR)</a></li>
	</ul>
</li>
	<li class="et_pb_menu_page_id-226090 menu-item menu-item-type-post_type menu-item-object-page menu-item-229927"><a href="https://www.empowersemi.com/ecap/">Silicon Capacitors</a></li>
</ul>
</li>
<li class="et_pb_menu_page_id-256407 menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-256407"><a href="#">Design Resources</a>
<ul class="sub-menu">
	<li class="et_pb_menu_page_id-257794 menu-item menu-item-type-post_type menu-item-object-page menu-item-258443"><a href="https://www.empowersemi.com/application-notes/">Application Notes</a></li>
	<li class="et_pb_menu_page_id-256420 menu-item menu-item-type-post_type menu-item-object-page menu-item-256429"><a href="https://www.empowersemi.com/videos/">Video Library</a></li>
	<li class="et_pb_menu_page_id-261749 menu-item menu-item-type-custom menu-item-object-custom menu-item-261749"><a href="https://www.empowersemi.com/wp-content/uploads/2023/09/FPGA-Power-Solutions-Brochure.pdf" data-lf-fd-inspected-xz1a5d7ow0wdp3k2="true">FPGA Power Solutions Brochure</a></li>
	<li class="et_pb_menu_page_id-256814 menu-item menu-item-type-post_type menu-item-object-page menu-item-257679"><a href="https://www.empowersemi.com/intel-enpirion-power-soc-cross-reference-selector/">Intel Enpirion Replacements</a></li>
	<li class="et_pb_menu_page_id-255547 menu-item menu-item-type-post_type menu-item-object-page menu-item-255676"><a href="https://www.empowersemi.com/inductor-design-request/">Inductor Design Request</a></li>
	<li class="et_pb_menu_page_id-264282 menu-item menu-item-type-post_type menu-item-object-page menu-item-264820"><a href="https://www.empowersemi.com/partner-reference-designs/amd-xilinx-ep71xx/">AMD Xilinx EP71xx Reference Designs</a></li>
</ul>
</li>
<li class="et_pb_menu_page_id-24950 menu-item menu-item-type-custom menu-item-object-custom menu-item-24950"><a href="https://www.empowersemi.com/applications/">Applications</a></li>
<li class="et_pb_menu_page_id-25017 menu-item menu-item-type-custom menu-item-object-custom current-menu-item current-menu-ancestor current-menu-parent menu-item-has-children menu-item-25017"><a href="https://www.empowersemi.com/technology/" aria-current="page">Technology</a>
<ul class="sub-menu">
	<li class="et_pb_menu_page_id-25190 menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-25190 current_page_item menu-item-255231"><a href="https://www.empowersemi.com/technology/" aria-current="page">Technology</a></li>
	<li class="et_pb_menu_page_id-254843 menu-item menu-item-type-post_type menu-item-object-page menu-item-255210"><a href="https://www.empowersemi.com/integrated-voltage-regulators/">What is an Integrated Voltage Regulator?</a></li>
	<li class="et_pb_menu_page_id-255774 menu-item menu-item-type-post_type menu-item-object-page menu-item-255977"><a href="https://www.empowersemi.com/an-introduction-to-e-cap-silicon-capacitors/">An Introduction to ECAP Silicon Capacitors</a></li>
</ul>
</li>
<li class="et_pb_menu_page_id-220240 menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-220273"><a href="https://www.empowersemi.com/news/">News</a>
<ul class="sub-menu">
	<li class="et_pb_menu_page_id-220368 menu-item menu-item-type-custom menu-item-object-custom menu-item-220368"><a href="https://www.empowersemi.com/news/">Empower News</a></li>
	<li class="et_pb_menu_page_id-220292 menu-item menu-item-type-post_type menu-item-object-page menu-item-220337"><a href="https://www.empowersemi.com/empower-in-the-news/">In The News</a></li>
</ul>
</li>
<li class="et_pb_menu_page_id-24958 menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-25007"><a href="https://www.empowersemi.com/about-us/">About Us</a>
<ul class="sub-menu">
	<li class="et_pb_menu_page_id-255551 menu-item menu-item-type-post_type menu-item-object-page menu-item-255633"><a href="https://www.empowersemi.com/board-of-directors/">Board of Directors</a></li>
	<li class="et_pb_menu_page_id-24958 menu-item menu-item-type-post_type menu-item-object-page menu-item-255230"><a href="https://www.empowersemi.com/about-us/">About Us</a></li>
	<li class="et_pb_menu_page_id-254786 menu-item menu-item-type-post_type menu-item-object-page menu-item-255066"><a href="https://www.empowersemi.com/environment-social-governance/">Environment &amp; Governance</a></li>
	<li class="et_pb_menu_page_id-255746 menu-item menu-item-type-custom menu-item-object-custom menu-item-255746"><a target="_blank" href="https://www.empowersemi.com/wp-content/uploads/2024/12/Empower-Corporate-Brochure-November-2024.pdf" data-lf-fd-inspected-xz1a5d7ow0wdp3k2="true">Download the Empower Brochure</a></li>
</ul>
</li>
<li class="et_pb_menu_page_id-219709 menu-item menu-item-type-post_type menu-item-object-page menu-item-219920"><a href="https://www.empowersemi.com/careers/">Careers</a></li>
<li class="et_pb_menu_page_id-25071 menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-25088"><a href="https://www.empowersemi.com/contact-us/">Contact us</a>
<ul class="sub-menu">
	<li class="et_pb_menu_page_id-264050 menu-item menu-item-type-custom menu-item-object-custom menu-item-264050"><a href="https://www.empowersemi.com/contact-us/#corporate">Corporate Offices</a></li>
	<li class="et_pb_menu_page_id-264051 menu-item menu-item-type-custom menu-item-object-custom menu-item-264051"><a href="https://www.empowersemi.com/contact-us/#sales">Sales Representatives</a></li>
	<li class="et_pb_menu_page_id-264052 menu-item menu-item-type-custom menu-item-object-custom menu-item-264052"><a href="https://www.empowersemi.com/contact-us/#distributors">Distributors</a></li>
</ul>
</li>
<li class="lang-item lang-item-16 lang-item-en current-lang lang-item-first menu-item menu-item-type-custom menu-item-object-custom menu-item-255050-en"><a href="https://www.empowersemi.com/technology/" hreflang="en-US" lang="en-US">En</a></li>
<li class="lang-item lang-item-20 lang-item-zh menu-item menu-item-type-custom menu-item-object-custom menu-item-255050-zh"><a href="https://www.empowersemi.com/zh/technology-cn-3/" hreflang="zh-CN" lang="zh-CN">中</a></li>
</ul></nav>
							</div>
							
							
							<div class="et_mobile_nav_menu">
				<div class="mobile_nav closed">
					<span class="mobile_menu_bar"></span>
				<ul id="mobile_menu1" class="et_mobile_menu"><li class="et_pb_menu_page_id-229928 menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-229928 et_first_mobile_item"><a href="#">Products</a>
<ul class="sub-menu">
	<li class="et_pb_menu_page_id-256390 menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-256390"><a href="https://www.empowersemi.com/integrated-voltage-regulators-ivr/">Power Conversion</a>
	<ul class="sub-menu">
		<li class="et_pb_menu_page_id-256357 menu-item menu-item-type-post_type menu-item-object-page menu-item-256392"><a href="https://www.empowersemi.com/3-3v-integrated-voltage-regulators-ivr/">3.3V Integrated Voltage Regulators (IVR)</a></li>
		<li class="et_pb_menu_page_id-256362 menu-item menu-item-type-post_type menu-item-object-page menu-item-256391"><a href="https://www.empowersemi.com/1-8v-integrated-voltage-regulators-ivr/">1.8V Integrated Voltage Regulators (IVR)</a></li>
	</ul>
</li>
	<li class="et_pb_menu_page_id-226090 menu-item menu-item-type-post_type menu-item-object-page menu-item-229927"><a href="https://www.empowersemi.com/ecap/">Silicon Capacitors</a></li>
</ul>
</li>
<li class="et_pb_menu_page_id-256407 menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-256407"><a href="#">Design Resources</a>
<ul class="sub-menu">
	<li class="et_pb_menu_page_id-257794 menu-item menu-item-type-post_type menu-item-object-page menu-item-258443"><a href="https://www.empowersemi.com/application-notes/">Application Notes</a></li>
	<li class="et_pb_menu_page_id-256420 menu-item menu-item-type-post_type menu-item-object-page menu-item-256429"><a href="https://www.empowersemi.com/videos/">Video Library</a></li>
	<li class="et_pb_menu_page_id-261749 menu-item menu-item-type-custom menu-item-object-custom menu-item-261749"><a href="https://www.empowersemi.com/wp-content/uploads/2023/09/FPGA-Power-Solutions-Brochure.pdf" data-lf-fd-inspected-xz1a5d7ow0wdp3k2="true">FPGA Power Solutions Brochure</a></li>
	<li class="et_pb_menu_page_id-256814 menu-item menu-item-type-post_type menu-item-object-page menu-item-257679"><a href="https://www.empowersemi.com/intel-enpirion-power-soc-cross-reference-selector/">Intel Enpirion Replacements</a></li>
	<li class="et_pb_menu_page_id-255547 menu-item menu-item-type-post_type menu-item-object-page menu-item-255676"><a href="https://www.empowersemi.com/inductor-design-request/">Inductor Design Request</a></li>
	<li class="et_pb_menu_page_id-264282 menu-item menu-item-type-post_type menu-item-object-page menu-item-264820"><a href="https://www.empowersemi.com/partner-reference-designs/amd-xilinx-ep71xx/">AMD Xilinx EP71xx Reference Designs</a></li>
</ul>
</li>
<li class="et_pb_menu_page_id-24950 menu-item menu-item-type-custom menu-item-object-custom menu-item-24950"><a href="https://www.empowersemi.com/applications/">Applications</a></li>
<li class="et_pb_menu_page_id-25017 menu-item menu-item-type-custom menu-item-object-custom current-menu-item current-menu-ancestor current-menu-parent menu-item-has-children menu-item-25017 et-show-dropdown et-hover"><a href="https://www.empowersemi.com/technology/" aria-current="page">Technology</a>
<ul class="sub-menu">
	<li class="et_pb_menu_page_id-25190 menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-25190 current_page_item menu-item-255231"><a href="https://www.empowersemi.com/technology/" aria-current="page">Technology</a></li>
	<li class="et_pb_menu_page_id-254843 menu-item menu-item-type-post_type menu-item-object-page menu-item-255210"><a href="https://www.empowersemi.com/integrated-voltage-regulators/">What is an Integrated Voltage Regulator?</a></li>
	<li class="et_pb_menu_page_id-255774 menu-item menu-item-type-post_type menu-item-object-page menu-item-255977"><a href="https://www.empowersemi.com/an-introduction-to-e-cap-silicon-capacitors/">An Introduction to ECAP Silicon Capacitors</a></li>
</ul>
</li>
<li class="et_pb_menu_page_id-220240 menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-220273"><a href="https://www.empowersemi.com/news/">News</a>
<ul class="sub-menu">
	<li class="et_pb_menu_page_id-220368 menu-item menu-item-type-custom menu-item-object-custom menu-item-220368"><a href="https://www.empowersemi.com/news/">Empower News</a></li>
	<li class="et_pb_menu_page_id-220292 menu-item menu-item-type-post_type menu-item-object-page menu-item-220337"><a href="https://www.empowersemi.com/empower-in-the-news/">In The News</a></li>
</ul>
</li>
<li class="et_pb_menu_page_id-24958 menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-25007"><a href="https://www.empowersemi.com/about-us/">About Us</a>
<ul class="sub-menu">
	<li class="et_pb_menu_page_id-255551 menu-item menu-item-type-post_type menu-item-object-page menu-item-255633"><a href="https://www.empowersemi.com/board-of-directors/">Board of Directors</a></li>
	<li class="et_pb_menu_page_id-24958 menu-item menu-item-type-post_type menu-item-object-page menu-item-255230"><a href="https://www.empowersemi.com/about-us/">About Us</a></li>
	<li class="et_pb_menu_page_id-254786 menu-item menu-item-type-post_type menu-item-object-page menu-item-255066"><a href="https://www.empowersemi.com/environment-social-governance/">Environment &amp; Governance</a></li>
	<li class="et_pb_menu_page_id-255746 menu-item menu-item-type-custom menu-item-object-custom menu-item-255746"><a target="_blank" href="https://www.empowersemi.com/wp-content/uploads/2024/12/Empower-Corporate-Brochure-November-2024.pdf" data-lf-fd-inspected-xz1a5d7ow0wdp3k2="true">Download the Empower Brochure</a></li>
</ul>
</li>
<li class="et_pb_menu_page_id-219709 menu-item menu-item-type-post_type menu-item-object-page menu-item-219920"><a href="https://www.empowersemi.com/careers/">Careers</a></li>
<li class="et_pb_menu_page_id-25071 menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-25088"><a href="https://www.empowersemi.com/contact-us/">Contact us</a>
<ul class="sub-menu">
	<li class="et_pb_menu_page_id-264050 menu-item menu-item-type-custom menu-item-object-custom menu-item-264050"><a href="https://www.empowersemi.com/contact-us/#corporate">Corporate Offices</a></li>
	<li class="et_pb_menu_page_id-264051 menu-item menu-item-type-custom menu-item-object-custom menu-item-264051"><a href="https://www.empowersemi.com/contact-us/#sales">Sales Representatives</a></li>
	<li class="et_pb_menu_page_id-264052 menu-item menu-item-type-custom menu-item-object-custom menu-item-264052"><a href="https://www.empowersemi.com/contact-us/#distributors">Distributors</a></li>
</ul>
</li>
<li class="lang-item lang-item-16 lang-item-en current-lang lang-item-first menu-item menu-item-type-custom menu-item-object-custom menu-item-255050-en"><a href="https://www.empowersemi.com/technology/" hreflang="en-US" lang="en-US">En</a></li>
<li class="lang-item lang-item-20 lang-item-zh menu-item menu-item-type-custom menu-item-object-custom menu-item-255050-zh"><a href="https://www.empowersemi.com/zh/technology-cn-3/" hreflang="zh-CN" lang="zh-CN">中</a></li>
</ul></div>
			</div>
						</div>
						
					</div>
				</div>
			</div>
				
				
				
				
			</div>
				
				
			</div>		</div>
	</header>
	<div id="et-main-area">
	
<div id="main-content">


			
				<article id="post-25190" class="post-25190 page type-page status-publish hentry">

				
					<div class="entry-content">
					<div class="et-l et-l--post">
			<div class="et_builder_inner_content et_pb_gutters3">
		<div class="et_pb_section et_pb_section_6 et_pb_with_background et_section_regular">
				
				
				
				
				
				
				<div class="et_pb_row et_pb_row_6">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_6  et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				
				
				<div class="et_pb_module et_pb_image et_pb_image_0">
				
				
				
				
				<span class="et_pb_image_wrap "><img fetchpriority="high" decoding="async" width="576" height="200" src="Technology%20_%20Empower%20Semiconductor_files/header-empowered-tech.webp" alt="" title="header-empowered-tech" srcset="Technology%20_%20Empower%20Semiconductor_files/header-empowered-tech.webp 576w, Technology%20_%20Empower%20Semiconductor_files/header-empowered-tech-480x167.png 480w" sizes="(min-width: 0px) and (max-width: 480px) 480px, (min-width: 481px) 576px, 100vw" class="wp-image-219910"></span>
			</div>
			</div>
				
				
				
				
			</div>
				
				
			</div><div class="et_pb_section et_pb_section_8 et_section_regular">
				
				
				
				
				
				
				<div class="et_pb_row et_pb_row_7">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_7  et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				
				
				<div class="et_pb_module df_adh_heading df_adh_heading_0">
				
				
				
				
				
				
				<div class="et_pb_module_inner">
					<div class="df-heading-container">
                
                
                <h3 class="df-heading"><span class="prefix">What is an Integrated Voltage Regulator (IVR)?</span>  </h3>
                <div class="df-heading-divider"><div class="df-divider-line"></div></div>
            </div>
				</div>
			</div><div class="et_pb_module et_pb_text et_pb_text_6  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><p>An IVR is a high-performance 
switching voltage regulator that eliminates or integrates all discrete 
components into a single device.</p>
<p>Empower Semiconductor develops high-frequency Integrated Voltage 
Regulators (IVRs) entirely on the industry’s most advanced CMOS 
process.&nbsp; These IVR products fully integrate ALL power supply 
discrete components, thereby simplifying the design process and 
shrinking the PCB area consumed by power management.</p>
<p>By using an advanced CMOS geometry platform, the Empower 
Semiconductor products can also be integrated directly into a SoC 
package to further reduce the power area and energy consumed. In 
comparison to today’s state-of-the-art power management ICs, Empower’s 
products enable:</p>
<p>&nbsp;</p>
<ul>
<li><strong>Significant area reduction consolidating all discrete components</strong></li>
<li><strong>Higher transient accuracy with 100x faster settling time</strong></li>
<li><strong>Nanosecond speed DVS delivering up to 50% energy savings</strong></li>
<li><strong>Advanced CMOS process allows for SoC Integration capability</strong></li>
</ul></div>
			</div><div class="et_pb_module df_adh_heading df_adh_heading_1">
				
				
				
				
				
				
				<div class="et_pb_module_inner">
					<div class="df-heading-container">
                
                
                <h3 class="df-heading"><span class="prefix">3x Area Reduction with Zero Discrete Components</span>  </h3>
                <div class="df-heading-divider"><div class="df-divider-line"></div></div>
            </div>
				</div>
			</div><div class="et_pb_module et_pb_text et_pb_text_7  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><h2></h2>
<p>Say goodbye to discrete inductors, capacitors and resistors!&nbsp; 
Empower either eliminates the need for the components altogether or 
integrates them completely into the package.</p>
<p>All difficult design decisions are made using the Empowered Development Tools.</p>
<p>Through the optimization, coordination, and combination of 
technologies by Empower the user can simply select their operating 
preferences with the GUI to configure the device using the high-speed 
I3C bus.</p>
<p>&nbsp;</p></div>
			</div><div class="et_pb_module et_pb_video et_pb_video_0">
				
				
				
				
				<div class="et_pb_video_box">
				<video controls="controls">
					<source type="video/mp4" src="Technology%20_%20Empower%20Semiconductor_files/Empower-Video-2023.mp4">
					
				</video></div>
				<div style="background-image: url(&quot;https://www.empowersemi.com/wp-content/uploads/2020/04/40-1-before-and-after-3-web.jpg&quot;);" class="et_pb_video_overlay lazyloaded" data-bg-image="url(https://www.empowersemi.com/wp-content/uploads/2020/04/40-1-before-and-after-3-web.jpg)"><div class="et_pb_video_overlay_hover"><a href="#" class="et_pb_video_play"></a></div></div>
			</div><div class="et_pb_module df_adh_heading df_adh_heading_2">
				
				
				
				
				
				
				<div class="et_pb_module_inner">
					<div class="df-heading-container">
                
                
                <h3 class="df-heading"><span class="prefix">Higher Transient Accuracy with 100x Faster Settling Time</span>  </h3>
                <div class="df-heading-divider"><div class="df-divider-line"></div></div>
            </div>
				</div>
			</div><div class="et_pb_module et_pb_text et_pb_text_8  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner">Traditional DC/DC converters must 
operate at low frequencies (0.3MHz – 3MHz) to achieve high 
efficiency.&nbsp; The low operating frequency means low bandwidth with 
large output and input filtering to achieve reasonable transient 
response.&nbsp; Several large or bulky output capacitors are typically 
placed in parallel to obtain 100μF or more.<p></p>
<p>Empower’s wide bandwidth regulators enable high accuracy voltages 
during full scale and extremely fast transients.&nbsp; Eliminating the 
large capacitors allows the Empower IVR’s output voltage to drop by 1/3 
or less with recovery times 100x faster versus current best in class 
DC/DC converters.</p></div>
			</div><div class="et_pb_module df_adh_heading df_adh_heading_3">
				
				
				
				
				
				
				<div class="et_pb_module_inner">
					<div class="df-heading-container">
                
                
                <h3 class="df-heading"><span class="prefix">1,000x Faster DVS Can Lead to 50% Energy Savings</span>  </h3>
                <div class="df-heading-divider"><div class="df-divider-line"></div></div>
            </div>
				</div>
			</div><div class="et_pb_module et_pb_text et_pb_text_9  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner">Existing power management ICs (legacy 
slow power management) are too slow to react to changing system voltage 
requirements.&nbsp; As power is proportional to voltage squared, 
significant power is wasted with the excess voltage.<p></p>
<p>Empower IVR products exhibit ultra-fast dynamic voltage scaling 
(&gt;1000x faster than the current best in class power management) and 
enable processor power state changes in <b><i>nanoseconds</i></b>. Nearly instantaneous voltage delivery eliminates the excess voltage &amp; wasted power.</p></div>
			</div><div class="et_pb_module et_pb_image et_pb_image_1">
				
				
				
				
				<span class="et_pb_image_wrap "><img decoding="async" width="935" height="587" data-src="https://www.empowersemi.com/wp-content/uploads/2020/04/Graph-and-chip6.jpg" alt="" title="Graph and chip6" data-srcset="https://www.empowersemi.com/wp-content/uploads/2020/04/Graph-and-chip6.jpg 935w, https://www.empowersemi.com/wp-content/uploads/2020/04/Graph-and-chip6-480x301.jpg 480w" data-sizes="(min-width: 0px) and (max-width: 480px) 480px, (min-width: 481px) 935px, 100vw" class="wp-image-219736 ls-is-cached lazyloaded" src="Technology%20_%20Empower%20Semiconductor_files/Graph-and-chip6.jpg" style="--smush-placeholder-width: 935px; --smush-placeholder-aspect-ratio: 935/587;" sizes="(min-width: 0px) and (max-width: 480px) 480px, (min-width: 481px) 935px, 100vw" srcset="Technology%20_%20Empower%20Semiconductor_files/Graph-and-chip6.jpg 935w, Technology%20_%20Empower%20Semiconductor_files/Graph-and-chip6-480x301.jpg 480w"></span>
			</div>
			</div>
				
				
				
				
			</div><div class="et_pb_row et_pb_row_8">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_8  et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				
				
				<div class="et_pb_module et_pb_divider et_pb_divider_0 et_pb_divider_position_ et_pb_space"><div class="et_pb_divider_internal"></div></div><div class="et_pb_module et_pb_image et_pb_image_2">
				
				
				
				
				<span class="et_pb_image_wrap "><img decoding="async" width="400" height="136" data-src="https://www.empowersemi.com/wp-content/uploads/2016/06/ECap-Colour-400px-1.jpg" alt="" title="ECap-Colour-400px" data-srcset="https://www.empowersemi.com/wp-content/uploads/2016/06/ECap-Colour-400px-1.jpg 400w, https://www.empowersemi.com/wp-content/uploads/2016/06/ECap-Colour-400px-1-300x102.jpg 300w, https://www.empowersemi.com/wp-content/uploads/2016/06/ECap-Colour-400px-1-20x7.jpg 20w" data-sizes="(max-width: 400px) 100vw, 400px" class="wp-image-229929 ls-is-cached lazyloaded" src="Technology%20_%20Empower%20Semiconductor_files/ECap-Colour-400px-1.jpg" style="--smush-placeholder-width: 400px; --smush-placeholder-aspect-ratio: 400/136;" sizes="(max-width: 400px) 100vw, 400px" srcset="Technology%20_%20Empower%20Semiconductor_files/ECap-Colour-400px-1.jpg 400w, Technology%20_%20Empower%20Semiconductor_files/ECap-Colour-400px-1-300x102.jpg 300w, Technology%20_%20Empower%20Semiconductor_files/ECap-Colour-400px-1-20x7.jpg 20w"></span>
			</div><div class="et_pb_module df_adh_heading df_adh_heading_4">
				
				
				
				
				
				
				<div class="et_pb_module_inner">
					<div class="df-heading-container">
                
                
                <h3 class="df-heading"><span class="prefix">The Highest Performance, Smallest Size, and Most Configurable Capacitor Technology Platform Ever!</span>  </h3>
                <div class="df-heading-divider"><div class="df-divider-line"></div></div>
            </div>
				</div>
			</div><div class="et_pb_module et_pb_text et_pb_text_10  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><p>Empowers E-CAP™ is a Revolutionary New Entry in the Capacitor Industry. Find out more by clicking below.</p></div>
			</div><div class="et_pb_button_module_wrapper et_pb_button_0_wrapper et_pb_button_alignment_center et_pb_module  dbdb-icon-on-right dbdb-icon-on-hover">
				<a class="et_pb_button et_pb_button_0 et_pb_bg_layout_light" href="https://www.empowersemi.com/ecap-new-capacitor-silicon-revolution/">Click Here for E-CAP™</a>
			</div>
			</div>
				
				
				
				
			</div>
				
				
			</div>		</div>
	</div>
						</div>

				
				</article>

			

</div>

	<footer class="et-l et-l--footer">
			<div class="et_builder_inner_content et_pb_gutters3"><div class="et_pb_section et_pb_section_0_tb_footer et_pb_with_background et_section_regular">
				
				
				
				
				
				
				<div class="et_pb_row et_pb_row_0_tb_footer">
				<div class="et_pb_column et_pb_column_1_3 et_pb_column_0_tb_footer  et_pb_css_mix_blend_mode_passthrough">
				
				
				
				
				<div class="et_pb_module et_pb_image et_pb_image_0_tb_footer">
				
				
				
				
				<a href="https://www.empowersemi.com/"><span class="et_pb_image_wrap "><img decoding="async" data-src="https://www.empowersemi.com/wp-content/uploads/2025/03/empower_logo-white.svg" alt="" title="empower_logo-white" class="wp-image-265094 lazyloaded" src="Technology%20_%20Empower%20Semiconductor_files/empower_logo-white.svg"></span></a>
			</div><div class="et_pb_module et_pb_text et_pb_text_0_tb_footer  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><p>&nbsp;<a href="https://www.empowersemi.com/privacy-policy">Privacy Policy</a> | <a href="https://www.empowersemi.com/terms-of-use/">Terms &amp; Conditions</a></p></div>
			</div><div class="et_pb_module et_pb_text et_pb_text_1_tb_footer  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><p>&nbsp;</p>
<p>© Empower Semiconductor 2025</p></div>
			</div>
			</div><div class="et_pb_column et_pb_column_1_3 et_pb_column_1_tb_footer  et_pb_css_mix_blend_mode_passthrough">
				
				
				
				
				<div class="et_pb_module et_pb_text et_pb_text_2_tb_footer  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><p><strong>Empower Semiconductor</strong></p></div>
			</div><div class="et_pb_module et_pb_text et_pb_text_3_tb_footer  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><p><span>2700 Zanker Rd, Suite 168<br>San Jose, CA 95134, USA<br></span></p>
<p>Contact us at <span>+1-408-957-8750</span><br>or send an Email: <a href="mailto:info@empowersemi.com">info@empowersemi.com</a></p>
<div id="malwarebytes-root"></div></div>
			</div>
			</div><div class="et_pb_column et_pb_column_1_3 et_pb_column_2_tb_footer  et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				
				
				<div class="et_pb_module et_pb_text et_pb_text_4_tb_footer  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><p><strong>Find us on:</strong></p></div>
			</div><div class="et_pb_module et_pb_image et_pb_image_1_tb_footer">
				
				
				
				
				<a href="https://www.linkedin.com/company/empower-semiconductor/"><span class="et_pb_image_wrap "><img decoding="async" width="792" height="332" data-src="https://www.empowersemi.com/wp-content/uploads/2020/02/linkedin-1.png" alt="" title="" data-srcset="https://www.empowersemi.com/wp-content/uploads/2020/02/linkedin-1.png 792w, https://www.empowersemi.com/wp-content/uploads/2020/02/linkedin-1-480x201.png 480w" data-sizes="(min-width: 0px) and (max-width: 480px) 480px, (min-width: 481px) 792px, 100vw" class="wp-image-24964 ls-is-cached lazyloaded" src="Technology%20_%20Empower%20Semiconductor_files/linkedin-1.png" style="--smush-placeholder-width: 792px; --smush-placeholder-aspect-ratio: 792/332;" sizes="(min-width: 0px) and (max-width: 480px) 480px, (min-width: 481px) 792px, 100vw" srcset="Technology%20_%20Empower%20Semiconductor_files/linkedin-1.png 792w, Technology%20_%20Empower%20Semiconductor_files/linkedin-1-480x201.png 480w"></span></a>
			</div>
			</div>
				
				
				
				
			</div>
				
				
			</div>		</div>
	</footer>
		</div>

			
		</div>
		</div>

			<script>				
                    document.addEventListener('DOMContentLoaded', function () {
                        setTimeout(function(){
                            if( document.querySelectorAll('[name^=ct_checkjs]').length > 0 ) {
                                if (typeof apbct_public_sendREST === 'function' && typeof apbct_js_keys__set_input_value === 'function') {
                                    apbct_public_sendREST(
                                    'js_keys__get',
                                    { callback: apbct_js_keys__set_input_value })
                                }
                            }
                        },0)					    
                    })				
                </script>
		<script>
			window.RS_MODULES = window.RS_MODULES || {};
			window.RS_MODULES.modules = window.RS_MODULES.modules || {};
			window.RS_MODULES.waiting = window.RS_MODULES.waiting || [];
			window.RS_MODULES.defered = true;
			window.RS_MODULES.moduleWaiting = window.RS_MODULES.moduleWaiting || {};
			window.RS_MODULES.type = 'compiled';
		</script>
		    <script>
        jQuery(document).ready(function($) {
            $('.et_pb_slider.dbdb_slider_random').each(function() {
                var $slider = $(this);
                var $slidesContainer = $slider.find('.et_pb_slides');

                // Randomize the slides
                var $slides = $slidesContainer.children().sort(function() {
                    return Math.random() - 0.5;
                }).detach().appendTo($slidesContainer);

                // Remove the active class from existing slide
                $slides.removeClass('et-pb-active-slide');

                // Restore visibility to the slides
                $slides.css('visibility', 'visible');


                // Add the active class to the first slide
                $slides.first().addClass('et-pb-active-slide');
            });
        });
    </script>

    <script>
        jQuery(function($) {

            // Trigger counter refresh on first load
            $('.dbdb-gallery-with-image-count').each(function() {
                triggerSlideChanged($(this));
            });

            // Trigger counter refresh when the slide changes (due to arrow button clicked)
            $(document).on('mouseup', '.dbdb-gallery-with-image-count .et-pb-slider-arrows a, .dbdb-gallery-with-image-count .et-pb-controllers a', function() {
                var $gallery = $(this).closest('.dbdb-gallery-with-image-count');
                triggerSlideChanged($gallery);
            });

            function triggerSlideChanged($gallery) {
                $gallery.trigger('divi-booster:gallery-slide-changed');
            }

            // Update the counter when the slide has changed
            $(document).on('divi-booster:gallery-slide-changed', '.dbdb-gallery-with-image-count', function() {
                var $gallery = $(this);
                setTimeout(function() {
                    var currentIndex = $gallery.find('.et-pb-active-slide').index() + 1;
                    $gallery.find('.dbdb-slide-counter-active').text(currentIndex);
                }, 50);
            });

            // Set separator on lightbox count
            setTimeout(
                function() {
                    $('.et_pb_gallery_items').each(function() {
                        if ($(this).data('magnificPopup') && $(this).data('dbdb-image-count-separator')) {
                            $(this).data('magnificPopup').gallery.tCounter = '%curr%' + $(this).data('dbdb-image-count-separator') + '%total%';
                        }
                    });
                },
                0
            );
        });
    </script>
    
    <script>
        jQuery(document).ready(function($) {
            $(document).on('click', '.et_pb_gallery .et_pb_gallery_image a', function() {

                // Remove the old class
                $('body').removeClass(function(index, className) {
                    return (className.match(/(^|\s)et_pb_gallery_\d+_dbdb_lightbox_open/g) || []).join(' ');
                });

                // Add the new class
                var gallery_module_order = $(this).closest('.et_pb_gallery').attr('class').match(/et_pb_gallery_\d+/)[0];
                $('body').addClass(gallery_module_order + '_dbdb_lightbox_open');
            });
        });
    </script>

            <script>
                jQuery(function($){

                    
                });
            </script>
            <div id="fb-root"></div>
            
			<script type="text/javascript">
				var _paq = _paq || [];
								_paq.push(['trackPageView']);
								(function () {
					var u = "https://stats1.wpmudev.com/";
					_paq.push(['setTrackerUrl', u + 'track/']);
					_paq.push(['setSiteId', '89154']);
					var d   = document, g = d.createElement('script'), s = d.getElementsByTagName('script')[0];
					g.type  = 'text/javascript';
					g.async = true;
					g.defer = true;
					g.src   = 'https://stats.wpmucdn.com/analytics.js';
					s.parentNode.insertBefore(g, s);
				})();
			</script>
			
  <!--copyscapeskip-->
  <aside id="moove_gdpr_cookie_info_bar" class="moove-gdpr-align-center moove-gdpr-light-scheme gdpr_infobar_postion_bottom" aria-label="GDPR Cookie Banner" style="">
    <div class="moove-gdpr-info-bar-container">
      <div class="moove-gdpr-info-bar-content">
        
<div class="moove-gdpr-cookie-notice">
  <p>We are using cookies to give you the best experience on our website.<br>
You can find out more about which cookies we are using or switch them off in <button tabindex="0" data-href="#moove_gdpr_cookie_modal" class="change-settings-button">settings</button>.</p>
</div>
<!--  .moove-gdpr-cookie-notice -->        
<div class="moove-gdpr-button-holder">
		  <button class="mgbutton moove-gdpr-infobar-allow-all gdpr-fbo-0" aria-label="Accept" tabindex="1">Accept</button>
	  </div>
<!--  .button-container -->      </div>
      <!-- moove-gdpr-info-bar-content -->
    </div>
    <!-- moove-gdpr-info-bar-container -->
  </aside>
  <!-- #moove_gdpr_cookie_info_bar -->
  <!--/copyscapeskip-->
		<script type="application/javascript">
			(function() {
				var file     = ["https:\/\/www.empowersemi.com\/wp-content\/et-cache\/25190\/et-divi-dynamic-tb-254998-tb-24969-25190-late.css"];
				var handle   = document.getElementById('divi-style-inline-inline-css');
				var location = handle.parentNode;

				if (0===document.querySelectorAll('link[href="' + file + '"]').length) {
					var link  = document.createElement('link');
					link.rel  = 'stylesheet';
					link.id   = 'et-dynamic-late-css';
					link.href = file;

					location.insertBefore(link, handle.nextSibling);
				}
			})();
		</script>
		<script>document.addEventListener("DOMContentLoaded", function () {
  var elements = document.querySelectorAll(".et_pb_number_counter h3.title");
  elements.forEach(function (element) {
    if (element.textContent === "mm2") {
      element.innerHTML = "mm<sup>2</sup>";
    }
  });
});</script>    




<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/public-module-script-min.js" id="dvmd-tm-public-module-script-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/df-menu-ext-script.js" id="df-menu-ext-script-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/hooks.min.js" id="wp-hooks-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/i18n.min.js" id="wp-i18n-js"></script>
<script type="text/javascript" id="wp-i18n-js-after">
/* <![CDATA[ */
wp.i18n.setLocaleData( { 'text direction\u0004ltr': [ 'ltr' ] } );
/* ]]> */
</script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/jquery.form.min.js" id="jquery-form-js"></script>
<script type="text/javascript" id="flat-preloader-js-js-extra">
/* <![CDATA[ */
var flatPreloader = {"delayTime":"500","showPreloaderInstantly":"","host":"www.empowersemi.com","ignores":["^https?:\\\/\\\/[^\\\/]+\\\/technology\\\/(#.*)?$","^https\\:\\\/\\\/www\\.empowersemi\\.com\\\/wp\\-admin\\\/","^https\\:\\\/\\\/www\\.empowersemi\\.com[^?#]+\\.php","\\\/wp\\-content",".*\\?.+","^\\\/technology\\\/(#.*)?$","^#.*","^mailto:.*","^tel:.*"],"display":"custom"};
/* ]]> */
</script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/flat-preloader.js" id="flat-preloader-js-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/rbtools.min.js" defer="defer" async="" id="tp-tools-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/rs6.min.js" defer="defer" async="" id="revmin-js"></script>
<script type="text/javascript" id="divi-custom-script-js-extra">
/* <![CDATA[ */
var DIVI = {"item_count":"%d Item","items_count":"%d Items"};
var et_builder_utils_params = {"condition":{"diviTheme":true,"extraTheme":false},"scrollLocations":["app","top"],"builderScrollLocations":{"desktop":"app","tablet":"app","phone":"app"},"onloadScrollLocation":"app","builderType":"fe"};
var et_frontend_scripts = {"builderCssContainerPrefix":"#et-boc","builderCssLayoutPrefix":"#et-boc .et-l"};
var et_pb_custom = {"ajaxurl":"https:\/\/www.empowersemi.com\/wp-admin\/admin-ajax.php","images_uri":"https:\/\/www.empowersemi.com\/wp-content\/themes\/Divi\/images","builder_images_uri":"https:\/\/www.empowersemi.com\/wp-content\/themes\/Divi\/includes\/builder\/images","et_frontend_nonce":"5cf7c4b2e1","subscription_failed":"Please, check the fields below to make sure you entered the correct information.","et_ab_log_nonce":"eaa6ca5c2e","fill_message":"Please, fill in the following fields:","contact_error_message":"Please, fix the following errors:","invalid":"Invalid email","captcha":"Captcha","prev":"Prev","previous":"Previous","next":"Next","wrong_captcha":"You entered the wrong number in captcha.","wrong_checkbox":"Checkbox","ignore_waypoints":"no","is_divi_theme_used":"1","widget_search_selector":".widget_search","ab_tests":[],"is_ab_testing_active":"","page_id":"25190","unique_test_id":"","ab_bounce_rate":"5","is_cache_plugin_active":"yes","is_shortcode_tracking":"","tinymce_uri":"https:\/\/www.empowersemi.com\/wp-content\/themes\/Divi\/includes\/builder\/frontend-builder\/assets\/vendors","accent_color":"#2ea3f2","waypoints_options":[]};
var et_pb_box_shadow_elements = [];
/* ]]> */
</script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/scripts.min.js" id="divi-custom-script-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/fitvids.js" id="fitvids-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/frontend-bundle.min_004.js" id="section-popup-frontend-bundle-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/frontend-bundle.min_005.js" id="divi-modal-popup-frontend-bundle-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/frontend-bundle.min_003.js" id="divi-modules-table-maker-frontend-bundle-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/frontend-bundle.min.js" id="diviflash-frontend-bundle-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/frontend-bundle.min_002.js" id="revslider-divi-frontend-bundle-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/main_002.js" id="DiviMegaPro-main-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/main.helper.js" id="DiviMegaPro-main-helper-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/common.js" id="et-core-common-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/kite-modules.js" id="kitemodules-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/smush-lazy-load.min.js" id="smush-lazy-load-js"></script>
<script type="text/javascript" id="smush-lazy-load-js-after">
/* <![CDATA[ */
function rw() { Waypoint.refreshAll(); } window.addEventListener( 'lazybeforeunveil', rw, false); window.addEventListener( 'lazyloaded', rw, false);
/* ]]> */
</script>
<script type="text/javascript" id="moove_gdpr_frontend-js-extra">
/* <![CDATA[ */
var moove_frontend_gdpr_scripts = {"ajaxurl":"https:\/\/www.empowersemi.com\/wp-admin\/admin-ajax.php","post_id":"25190","plugin_dir":"https:\/\/www.empowersemi.com\/wp-content\/plugins\/gdpr-cookie-compliance","show_icons":"all","is_page":"1","ajax_cookie_removal":"false","strict_init":"1","enabled_default":{"third_party":1,"advanced":0},"geo_location":"false","force_reload":"false","is_single":"","hide_save_btn":"false","current_user":"0","cookie_expiration":"365","script_delay":"2000","close_btn_action":"1","close_btn_rdr":"","scripts_defined":"{\"cache\":true,\"header\":\"\",\"body\":\"\",\"footer\":\"\",\"thirdparty\":{\"header\":\"<script data-gdpr> (function(ss,ex){ window.ldfdr=window.ldfdr||function(){(ldfdr._q=ldfdr._q||[]).push([].slice.call(arguments));}; (function(d,s){ fs=d.getElementsByTagName(s)[0]; function ce(src){ var cs=d.createElement(s); cs.src=src; cs.async=1; fs.parentNode.insertBefore(cs,fs); }; ce('https:\\\/\\\/sc.lfeeder.com\\\/lftracker_v1_'+ss+(ex?'_'+ex:'')+'.js'); })(document,'script'); })('Xz1A5d7Ow0wdP3k2'); <\\\/script>\\t\\t\\t\\t<!-- Google tag (gtag.js) - Google Analytics 4 -->\\n\\t\\t\\t\\t<script data-gdpr src=\\\"https:\\\/\\\/www.googletagmanager.com\\\/gtag\\\/js?id=G-YSWE9FLBZ4\\\" data-type=\\\"gdpr-integration\\\"><\\\/script>\\n\\t\\t\\t\\t<script data-gdpr data-type=\\\"gdpr-integration\\\">\\n\\t\\t\\t\\t  window.dataLayer = window.dataLayer || [];\\n\\t\\t\\t\\t  function gtag(){dataLayer.push(arguments);}\\n\\t\\t\\t\\t  gtag('js', new Date());\\n\\n\\t\\t\\t\\t  gtag('config', 'G-YSWE9FLBZ4');\\n\\t\\t\\t\\t<\\\/script>\\n\\t\\t\\t\\t\\t\\t\\t\\t<script data-gdpr>\\n\\t\\t\\t\\t\\tgtag('consent', 'update', {\\n\\t\\t\\t      'ad_storage': 'granted',\\n\\t\\t\\t\\t    'ad_user_data': 'granted',\\n\\t\\t\\t\\t    'ad_personalization': 'granted',\\n\\t\\t\\t\\t    'analytics_storage': 'granted',\\n\\t\\t\\t\\t    'personalization_storage': 'granted',\\n\\t\\t\\t\\t\\t\\t'security_storage': 'granted',\\n\\t\\t\\t\\t\\t\\t'functionality_storage': 'granted',\\n\\t\\t\\t    });\\n\\n\\t\\t\\t    dataLayer.push({\\n\\t\\t\\t\\t\\t 'event': 'cookie_consent_update'\\n\\t\\t\\t\\t\\t});\\n\\t\\t\\t\\t<\\\/script>\\t\\n\\t\\t\\t\\t\",\"body\":\"\",\"footer\":\"\"},\"advanced\":{\"header\":\"\",\"body\":\"\",\"footer\":\"\"}}","gdpr_scor":"true","wp_lang":"_en","wp_consent_api":"false"};
/* ]]> */
</script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/main.js" id="moove_gdpr_frontend-js"></script>
<script type="text/javascript" id="moove_gdpr_frontend-js-after">
/* <![CDATA[ */
var gdpr_consent__strict = "true"
var gdpr_consent__thirdparty = "true"
var gdpr_consent__advanced = "false"
var gdpr_consent__cookies = "strict|thirdparty"
/* ]]> */
</script>
<script type="text/javascript" id="mediaelement-core-js-before">
/* <![CDATA[ */
var mejsL10n = {"language":"en","strings":{"mejs.download-file":"Download File","mejs.install-flash":"You are using a browser that does not have Flash player enabled or installed. Please turn on your Flash player plugin or download the latest version from https:\/\/get.adobe.com\/flashplayer\/","mejs.fullscreen":"Fullscreen","mejs.play":"Play","mejs.pause":"Pause","mejs.time-slider":"Time Slider","mejs.time-help-text":"Use Left\/Right Arrow keys to advance one second, Up\/Down arrows to advance ten seconds.","mejs.live-broadcast":"Live Broadcast","mejs.volume-help-text":"Use Up\/Down Arrow keys to increase or decrease volume.","mejs.unmute":"Unmute","mejs.mute":"Mute","mejs.volume-slider":"Volume Slider","mejs.video-player":"Video Player","mejs.audio-player":"Audio Player","mejs.captions-subtitles":"Captions\/Subtitles","mejs.captions-chapters":"Chapters","mejs.none":"None","mejs.afrikaans":"Afrikaans","mejs.albanian":"Albanian","mejs.arabic":"Arabic","mejs.belarusian":"Belarusian","mejs.bulgarian":"Bulgarian","mejs.catalan":"Catalan","mejs.chinese":"Chinese","mejs.chinese-simplified":"Chinese (Simplified)","mejs.chinese-traditional":"Chinese (Traditional)","mejs.croatian":"Croatian","mejs.czech":"Czech","mejs.danish":"Danish","mejs.dutch":"Dutch","mejs.english":"English","mejs.estonian":"Estonian","mejs.filipino":"Filipino","mejs.finnish":"Finnish","mejs.french":"French","mejs.galician":"Galician","mejs.german":"German","mejs.greek":"Greek","mejs.haitian-creole":"Haitian Creole","mejs.hebrew":"Hebrew","mejs.hindi":"Hindi","mejs.hungarian":"Hungarian","mejs.icelandic":"Icelandic","mejs.indonesian":"Indonesian","mejs.irish":"Irish","mejs.italian":"Italian","mejs.japanese":"Japanese","mejs.korean":"Korean","mejs.latvian":"Latvian","mejs.lithuanian":"Lithuanian","mejs.macedonian":"Macedonian","mejs.malay":"Malay","mejs.maltese":"Maltese","mejs.norwegian":"Norwegian","mejs.persian":"Persian","mejs.polish":"Polish","mejs.portuguese":"Portuguese","mejs.romanian":"Romanian","mejs.russian":"Russian","mejs.serbian":"Serbian","mejs.slovak":"Slovak","mejs.slovenian":"Slovenian","mejs.spanish":"Spanish","mejs.swahili":"Swahili","mejs.swedish":"Swedish","mejs.tagalog":"Tagalog","mejs.thai":"Thai","mejs.turkish":"Turkish","mejs.ukrainian":"Ukrainian","mejs.vietnamese":"Vietnamese","mejs.welsh":"Welsh","mejs.yiddish":"Yiddish"}};
/* ]]> */
</script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/mediaelement-and-player.min.js" id="mediaelement-core-js"></script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/mediaelement-migrate.min.js" id="mediaelement-migrate-js"></script>
<script type="text/javascript" id="mediaelement-js-extra">
/* <![CDATA[ */
var _wpmejsSettings = {"pluginPath":"\/wp-includes\/js\/mediaelement\/","classPrefix":"mejs-","stretching":"responsive","audioShortcodeLibrary":"mediaelement","videoShortcodeLibrary":"mediaelement"};
/* ]]> */
</script>
<script type="text/javascript" src="Technology%20_%20Empower%20Semiconductor_files/wp-mediaelement.min.js" id="wp-mediaelement-js"></script>
<style id="et-builder-module-design-tb-254998-tb-24969-deferred-25190-cached-inline-styles">.et_pb_section_0_tb_header.et_pb_section{padding-top:2px;padding-bottom:5px}.et_pb_row_0_tb_header.et_pb_row{padding-top:34px!important;padding-top:34px}.et_pb_row_0_tb_header,body #page-container .et-db #et-boc .et-l .et_pb_row_0_tb_header.et_pb_row,body.et_pb_pagebuilder_layout.single #page-container #et-boc .et-l .et_pb_row_0_tb_header.et_pb_row,body.et_pb_pagebuilder_layout.single.et_full_width_page #page-container #et-boc .et-l .et_pb_row_0_tb_header.et_pb_row{width:94%;max-width:1627px}.et_pb_image_0_tb_header{width:86%;max-width:350px;text-align:left;margin-left:0}.et_pb_image_0_tb_header .et_pb_image_wrap{display:block}.et_pb_menu_0_tb_header.et_pb_menu ul li a{font-family:'Poppins',Helvetica,Arial,Lucida,sans-serif;font-weight:600}.et_pb_menu_0_tb_header.et_pb_menu{background-color:#ffffff}.et_pb_menu_0_tb_header{margin-top:5px!important}.et_pb_menu_0_tb_header.et_pb_menu .nav li ul,.et_pb_menu_0_tb_header.et_pb_menu .et_mobile_menu,.et_pb_menu_0_tb_header.et_pb_menu .et_mobile_menu ul{background-color:#ffffff!important}.et_pb_menu_0_tb_header .et_pb_menu_inner_container>.et_pb_menu__logo-wrap,.et_pb_menu_0_tb_header .et_pb_menu__logo-slot{width:auto;max-width:100%}.et_pb_menu_0_tb_header .et_pb_menu_inner_container>.et_pb_menu__logo-wrap .et_pb_menu__logo img,.et_pb_menu_0_tb_header .et_pb_menu__logo-slot .et_pb_menu__logo-wrap img{height:auto;max-height:none}.et_pb_menu_0_tb_header .mobile_nav .mobile_menu_bar:before,.et_pb_menu_0_tb_header .et_pb_menu__icon.et_pb_menu__search-button,.et_pb_menu_0_tb_header .et_pb_menu__icon.et_pb_menu__close-search-button,.et_pb_menu_0_tb_header .et_pb_menu__icon.et_pb_menu__cart-button{color:#2ea3f2}.et_pb_image_0_tb_header.et_pb_module{margin-left:auto!important;margin-right:auto!important}@media only screen and (max-width:980px){.et_pb_image_0_tb_header .et_pb_image_wrap img{width:auto}}@media only screen and (max-width:767px){.et_pb_image_0_tb_header .et_pb_image_wrap img{width:auto}}.et_pb_section_0_tb_footer.et_pb_section{padding-top:15px;padding-right:0px;padding-bottom:30px;padding-left:0px;background-color:#0c0c0c!important}.et_pb_row_0_tb_footer.et_pb_row{padding-top:27px!important;padding-right:5px!important;padding-bottom:10px!important;padding-left:0px!important;padding-top:27px;padding-right:5px;padding-bottom:10px;padding-left:0px}.et_pb_image_0_tb_footer .et_pb_image_wrap img{min-height:33.8px}.et_pb_image_0_tb_footer{width:80%;text-align:left;margin-left:0}.et_pb_image_0_tb_footer .et_pb_image_wrap{display:block}.et_pb_text_0_tb_footer.et_pb_text,.et_pb_text_1_tb_footer.et_pb_text,.et_pb_text_2_tb_footer.et_pb_text,.et_pb_text_3_tb_footer.et_pb_text,.et_pb_text_4_tb_footer.et_pb_text{color:#ffffff!important}.et_pb_text_0_tb_footer,.et_pb_text_1_tb_footer,.et_pb_text_3_tb_footer{line-height:2em;font-size:14px;line-height:2em;padding-bottom:0px!important}.et_pb_image_1_tb_footer{margin-top:-31px!important;margin-bottom:0px!important;max-width:51%;text-align:left;margin-left:0}@media only screen and (max-width:980px){.et_pb_image_0_tb_footer .et_pb_image_wrap img,.et_pb_image_1_tb_footer .et_pb_image_wrap img{width:auto}.et_pb_image_1_tb_footer{text-align:center;margin-left:auto;margin-right:auto}}@media only screen and (max-width:767px){.et_pb_image_0_tb_footer .et_pb_image_wrap img,.et_pb_image_1_tb_footer .et_pb_image_wrap img{width:auto}}.et_pb_section_0,.et_pb_section_1,.et_pb_section_2,.et_pb_section_3,.et_pb_section_4{border-radius:14px 14px 14px 14px;overflow:hidden;border-top-width:1px;border-top-color:#ccd2db;z-index:10;box-shadow:0px 2px 18px 0px rgba(0,0,0,0.3)}.et_pb_section_0.et_pb_section,.et_pb_section_1.et_pb_section,.et_pb_section_2.et_pb_section,.et_pb_section_3.et_pb_section,.et_pb_section_4.et_pb_section{padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;margin-top:0px;margin-right:0px;margin-bottom:0px;margin-left:0px;background-color:#e7eaee!important}.et_pb_text_0,.et_pb_text_1,.et_pb_text_2,.et_pb_text_3,.et_pb_text_4,.et_pb_text_5{line-height:1.4em;font-size:14px;line-height:1.4em}.et_pb_section_5{border-radius:8px 8px 8px 8px;overflow:hidden;border-top-width:1px;border-top-color:#e0e0e0;z-index:10;box-shadow:0px 2px 18px 0px rgba(0,0,0,0.3)}.et_pb_section_5.et_pb_section{padding-top:0px;padding-bottom:0px;padding-left:0px;margin-top:0px;margin-right:0px;margin-bottom:0px;margin-left:0px;background-color:#e7eaee!important}div.et_pb_section.et_pb_section_6{background-image:url(https://www.empowersemi.com/wp-content/uploads/2020/02/hero-phone-1.jpg)!important}.et_pb_section_6.et_pb_section{padding-top:52px;padding-bottom:45px}.et_pb_image_0{text-align:left;margin-left:0}.et_pb_section_8.et_pb_section{padding-top:37px}.df_adh_heading_0 h1,.df_adh_heading_0 h2,.df_adh_heading_0 h3,.df_adh_heading_0 h4,.df_adh_heading_0 h5,.df_adh_heading_0 h6,.df_adh_heading_0 h1 span,.df_adh_heading_0 h2 span,.df_adh_heading_0 h3 span,.df_adh_heading_0 h4 span,.df_adh_heading_0 h5 span,.df_adh_heading_0 h6 span,.df_adh_heading_1 h1,.df_adh_heading_1 h2,.df_adh_heading_1 h3,.df_adh_heading_1 h4,.df_adh_heading_1 h5,.df_adh_heading_1 h6,.df_adh_heading_1 h1 span,.df_adh_heading_1 h2 span,.df_adh_heading_1 h3 span,.df_adh_heading_1 h4 span,.df_adh_heading_1 h5 span,.df_adh_heading_1 h6 span,.df_adh_heading_2 h1,.df_adh_heading_2 h2,.df_adh_heading_2 h3,.df_adh_heading_2 h4,.df_adh_heading_2 h5,.df_adh_heading_2 h6,.df_adh_heading_2 h1 span,.df_adh_heading_2 h2 span,.df_adh_heading_2 h3 span,.df_adh_heading_2 h4 span,.df_adh_heading_2 h5 span,.df_adh_heading_2 h6 span,.df_adh_heading_3 h1,.df_adh_heading_3 h2,.df_adh_heading_3 h3,.df_adh_heading_3 h4,.df_adh_heading_3 h5,.df_adh_heading_3 h6,.df_adh_heading_3 h1 span,.df_adh_heading_3 h2 span,.df_adh_heading_3 h3 span,.df_adh_heading_3 h4 span,.df_adh_heading_3 h5 span,.df_adh_heading_3 h6 span{font-family:'Poppins',Helvetica,Arial,Lucida,sans-serif!important;font-weight:700!important;font-size:64px!important;text-align:center!important}.df_adh_heading_0 .df-heading-dual_text,.df_adh_heading_1 .df-heading-dual_text,.df_adh_heading_2 .df-heading-dual_text,.df_adh_heading_3 .df-heading-dual_text,.df_adh_heading_4 .df-heading-dual_text{color:#e0e0e0!important}.df_adh_heading_0 span.prefix,.df_adh_heading_1 span.prefix,.df_adh_heading_2 span.prefix,.df_adh_heading_3 span.prefix,.df_adh_heading_4 span.prefix{font-size:26px!important}.df_adh_heading_0 .df-heading-divider .df-divider-line,.df_adh_heading_1 .df-heading-divider .df-divider-line,.df_adh_heading_2 .df-heading-divider .df-divider-line,.df_adh_heading_3 .df-heading-divider .df-divider-line,.df_adh_heading_4 .df-heading-divider .df-divider-line{margin-top:8px!important;top:calc(50% - 2.5px);height:5px;border-radius:0px}.df_adh_heading_0 .df-heading-divider .df-divider-line::before,.df_adh_heading_1 .df-heading-divider .df-divider-line::before,.df_adh_heading_2 .df-heading-divider .df-divider-line::before,.df_adh_heading_3 .df-heading-divider .df-divider-line::before,.df_adh_heading_4 .df-heading-divider .df-divider-line::before{border-top-style:solid!important;border-top-color:#005b8a!important;border-top-width:5px}.df_adh_heading_0 .df-heading-divider,.df_adh_heading_1 .df-heading-divider,.df_adh_heading_2 .df-heading-divider,.df_adh_heading_3 .df-heading-divider,.df_adh_heading_4 .df-heading-divider{max-width:120px;margin:0 auto}.df_adh_heading_0 .df-heading-divider::before,.df_adh_heading_1 .df-heading-divider::before,.df_adh_heading_2 .df-heading-divider::before,.df_adh_heading_3 .df-heading-divider::before,.df_adh_heading_4 .df-heading-divider::before{position:relative}.df_adh_heading_0 .df-heading-divider .df-divider-line:before,.df_adh_heading_1 .df-heading-divider .df-divider-line:before,.df_adh_heading_2 .df-heading-divider .df-divider-line:before,.df_adh_heading_3 .df-heading-divider .df-divider-line:before,.df_adh_heading_4 .df-heading-divider .df-divider-line:before{border-radius:0px}.df_adh_heading_0 .df-heading-divider span,.df_adh_heading_1 .df-heading-divider span,.df_adh_heading_2 .df-heading-divider span,.df_adh_heading_3 .df-heading-divider span,.df_adh_heading_4 .df-heading-divider span{font-size:18px}.df_adh_heading_0 .df-heading-divider .et-pb-icon,.df_adh_heading_0 .df-heading-divider img,.df_adh_heading_1 .df-heading-divider .et-pb-icon,.df_adh_heading_1 .df-heading-divider img,.df_adh_heading_2 .df-heading-divider .et-pb-icon,.df_adh_heading_2 .df-heading-divider img,.df_adh_heading_3 .df-heading-divider .et-pb-icon,.df_adh_heading_3 .df-heading-divider img,.df_adh_heading_4 .df-heading-divider .et-pb-icon,.df_adh_heading_4 .df-heading-divider img{background-color:rgba(0,0,0,0)!important}.df_adh_heading_0 .df-heading-divider .divider-image,.df_adh_heading_1 .df-heading-divider .divider-image,.df_adh_heading_2 .df-heading-divider .divider-image,.df_adh_heading_3 .df-heading-divider .divider-image,.df_adh_heading_4 .df-heading-divider .divider-image{max-width:100px}.df_adh_heading_0 .df-heading .prefix,.df_adh_heading_0 .df-heading .infix,.df_adh_heading_0 .df-heading .suffix,.df_adh_heading_1 .df-heading .prefix,.df_adh_heading_1 .df-heading .infix,.df_adh_heading_1 .df-heading .suffix,.df_adh_heading_2 .df-heading .prefix,.df_adh_heading_2 .df-heading .infix,.df_adh_heading_2 .df-heading .suffix,.df_adh_heading_3 .df-heading .prefix,.df_adh_heading_3 .df-heading .infix,.df_adh_heading_3 .df-heading .suffix,.df_adh_heading_4 .df-heading .prefix,.df_adh_heading_4 .df-heading .infix,.df_adh_heading_4 .df-heading .suffix{display:inline-block;max-width:100%}.et_pb_text_7 h2,.et_pb_text_8 h2,.et_pb_text_9 h2,.et_pb_text_10 h2{font-family:'Montserrat',Helvetica,Arial,Lucida,sans-serif;font-weight:700}.et_pb_video_0 .et_pb_video_overlay .et_pb_video_play{color:RGBA(255,255,255,0)}.et_pb_video_0 .et_pb_video_overlay_hover:hover{background-color:rgba(0,0,0,.6)}.et_pb_image_1,.et_pb_image_2{text-align:center}.et_pb_divider_0:before{border-top-color:#2ea3f2}.df_adh_heading_4 h1,.df_adh_heading_4 h2,.df_adh_heading_4 h3,.df_adh_heading_4 h4,.df_adh_heading_4 h5,.df_adh_heading_4 h6,.df_adh_heading_4 h1 span,.df_adh_heading_4 h2 span,.df_adh_heading_4 h3 span,.df_adh_heading_4 h4 span,.df_adh_heading_4 h5 span,.df_adh_heading_4 h6 span{font-family:'Poppins',Helvetica,Arial,Lucida,sans-serif!important;font-weight:700!important;font-size:64px!important;line-height:1.4em!important;text-align:center!important}body #page-container .et_pb_section .et_pb_button_0{color:#ffffff!important;background-color:#01c2eb}.et_pb_button_0,.et_pb_button_0:after{transition:all 300ms ease 0ms}@media only screen and (min-width:981px){.et_pb_image_0{width:30%}.et_pb_image_2{width:24%}}@media only screen and (max-width:980px){.et_pb_section_0,.et_pb_section_1,.et_pb_section_2,.et_pb_section_3,.et_pb_section_4{border-top-width:1px;border-top-color:#ccd2db}.et_pb_section_5{border-top-width:1px;border-top-color:#e0e0e0}.et_pb_image_0 .et_pb_image_wrap img,.et_pb_image_1 .et_pb_image_wrap img,.et_pb_image_2 .et_pb_image_wrap img{width:auto}.df_adh_heading_0 h1,.df_adh_heading_0 h2,.df_adh_heading_0 h3,.df_adh_heading_0 h4,.df_adh_heading_0 h5,.df_adh_heading_0 h6,.df_adh_heading_0 h1 span,.df_adh_heading_0 h2 span,.df_adh_heading_0 h3 span,.df_adh_heading_0 h4 span,.df_adh_heading_0 h5 span,.df_adh_heading_0 h6 span,.df_adh_heading_1 h1,.df_adh_heading_1 h2,.df_adh_heading_1 h3,.df_adh_heading_1 h4,.df_adh_heading_1 h5,.df_adh_heading_1 h6,.df_adh_heading_1 h1 span,.df_adh_heading_1 h2 span,.df_adh_heading_1 h3 span,.df_adh_heading_1 h4 span,.df_adh_heading_1 h5 span,.df_adh_heading_1 h6 span,.df_adh_heading_2 h1,.df_adh_heading_2 h2,.df_adh_heading_2 h3,.df_adh_heading_2 h4,.df_adh_heading_2 h5,.df_adh_heading_2 h6,.df_adh_heading_2 h1 span,.df_adh_heading_2 h2 span,.df_adh_heading_2 h3 span,.df_adh_heading_2 h4 span,.df_adh_heading_2 h5 span,.df_adh_heading_2 h6 span,.df_adh_heading_3 h1,.df_adh_heading_3 h2,.df_adh_heading_3 h3,.df_adh_heading_3 h4,.df_adh_heading_3 h5,.df_adh_heading_3 h6,.df_adh_heading_3 h1 span,.df_adh_heading_3 h2 span,.df_adh_heading_3 h3 span,.df_adh_heading_3 h4 span,.df_adh_heading_3 h5 span,.df_adh_heading_3 h6 span,.df_adh_heading_4 h1,.df_adh_heading_4 h2,.df_adh_heading_4 h3,.df_adh_heading_4 h4,.df_adh_heading_4 h5,.df_adh_heading_4 h6,.df_adh_heading_4 h1 span,.df_adh_heading_4 h2 span,.df_adh_heading_4 h3 span,.df_adh_heading_4 h4 span,.df_adh_heading_4 h5 span,.df_adh_heading_4 h6 span{font-size:48px!important}.df_adh_heading_0 .df-heading-divider .df-divider-line::before,.df_adh_heading_1 .df-heading-divider .df-divider-line::before,.df_adh_heading_2 .df-heading-divider .df-divider-line::before,.df_adh_heading_3 .df-heading-divider .df-divider-line::before,.df_adh_heading_4 .df-heading-divider .df-divider-line::before{border-top-width:5px!important}.df_adh_heading_0 .df-heading-divider .df-divider-line,.df_adh_heading_1 .df-heading-divider .df-divider-line,.df_adh_heading_2 .df-heading-divider .df-divider-line,.df_adh_heading_3 .df-heading-divider .df-divider-line,.df_adh_heading_4 .df-heading-divider .df-divider-line{height:5px!important;border-radius:0px!important}.df_adh_heading_0 .df-heading-divider,.df_adh_heading_1 .df-heading-divider,.df_adh_heading_2 .df-heading-divider,.df_adh_heading_3 .df-heading-divider,.df_adh_heading_4 .df-heading-divider{max-width:120px!important}.df_adh_heading_0 .df-heading-divider .df-divider-line:before,.df_adh_heading_1 .df-heading-divider .df-divider-line:before,.df_adh_heading_2 .df-heading-divider .df-divider-line:before,.df_adh_heading_3 .df-heading-divider .df-divider-line:before,.df_adh_heading_4 .df-heading-divider .df-divider-line:before{border-radius:0px!important}.df_adh_heading_0 .df-heading-divider span,.df_adh_heading_1 .df-heading-divider span,.df_adh_heading_2 .df-heading-divider span,.df_adh_heading_3 .df-heading-divider span,.df_adh_heading_4 .df-heading-divider span{font-size:18px!important}.df_adh_heading_0 .df-heading-divider .et-pb-icon,.df_adh_heading_0 .df-heading-divider img,.df_adh_heading_1 .df-heading-divider .et-pb-icon,.df_adh_heading_1 .df-heading-divider img,.df_adh_heading_2 .df-heading-divider .et-pb-icon,.df_adh_heading_2 .df-heading-divider img,.df_adh_heading_3 .df-heading-divider .et-pb-icon,.df_adh_heading_3 .df-heading-divider img,.df_adh_heading_4 .df-heading-divider .et-pb-icon,.df_adh_heading_4 .df-heading-divider img{background-color:rgba(0,0,0,0)!important}.df_adh_heading_0 .df-heading-divider .divider-image,.df_adh_heading_1 .df-heading-divider .divider-image,.df_adh_heading_2 .df-heading-divider .divider-image,.df_adh_heading_3 .df-heading-divider .divider-image,.df_adh_heading_4 .df-heading-divider .divider-image{max-width:100px!important}.df_adh_heading_0 .df-heading .prefix,.df_adh_heading_0 .df-heading .infix,.df_adh_heading_0 .df-heading .suffix,.df_adh_heading_1 .df-heading .prefix,.df_adh_heading_1 .df-heading .infix,.df_adh_heading_1 .df-heading .suffix,.df_adh_heading_2 .df-heading .prefix,.df_adh_heading_2 .df-heading .infix,.df_adh_heading_2 .df-heading .suffix,.df_adh_heading_3 .df-heading .prefix,.df_adh_heading_3 .df-heading .infix,.df_adh_heading_3 .df-heading .suffix,.df_adh_heading_4 .df-heading .prefix,.df_adh_heading_4 .df-heading .infix,.df_adh_heading_4 .df-heading .suffix{display:inline-block;max-width:100%}.et_pb_image_2{width:52%}body #page-container .et_pb_section .et_pb_button_0:after{display:inline-block;opacity:0}body #page-container .et_pb_section .et_pb_button_0:hover:after{opacity:1}}@media only screen and (max-width:767px){.et_pb_section_0,.et_pb_section_1,.et_pb_section_2,.et_pb_section_3,.et_pb_section_4{border-top-width:1px;border-top-color:#ccd2db}.et_pb_section_5{border-top-width:1px;border-top-color:#e0e0e0}.et_pb_image_0{width:65%}.et_pb_image_0 .et_pb_image_wrap img,.et_pb_image_1 .et_pb_image_wrap img,.et_pb_image_2 .et_pb_image_wrap img{width:auto}.df_adh_heading_0 h1,.df_adh_heading_0 h2,.df_adh_heading_0 h3,.df_adh_heading_0 h4,.df_adh_heading_0 h5,.df_adh_heading_0 h6,.df_adh_heading_0 h1 span,.df_adh_heading_0 h2 span,.df_adh_heading_0 h3 span,.df_adh_heading_0 h4 span,.df_adh_heading_0 h5 span,.df_adh_heading_0 h6 span,.df_adh_heading_1 h1,.df_adh_heading_1 h2,.df_adh_heading_1 h3,.df_adh_heading_1 h4,.df_adh_heading_1 h5,.df_adh_heading_1 h6,.df_adh_heading_1 h1 span,.df_adh_heading_1 h2 span,.df_adh_heading_1 h3 span,.df_adh_heading_1 h4 span,.df_adh_heading_1 h5 span,.df_adh_heading_1 h6 span,.df_adh_heading_2 h1,.df_adh_heading_2 h2,.df_adh_heading_2 h3,.df_adh_heading_2 h4,.df_adh_heading_2 h5,.df_adh_heading_2 h6,.df_adh_heading_2 h1 span,.df_adh_heading_2 h2 span,.df_adh_heading_2 h3 span,.df_adh_heading_2 h4 span,.df_adh_heading_2 h5 span,.df_adh_heading_2 h6 span,.df_adh_heading_3 h1,.df_adh_heading_3 h2,.df_adh_heading_3 h3,.df_adh_heading_3 h4,.df_adh_heading_3 h5,.df_adh_heading_3 h6,.df_adh_heading_3 h1 span,.df_adh_heading_3 h2 span,.df_adh_heading_3 h3 span,.df_adh_heading_3 h4 span,.df_adh_heading_3 h5 span,.df_adh_heading_3 h6 span,.df_adh_heading_4 h1,.df_adh_heading_4 h2,.df_adh_heading_4 h3,.df_adh_heading_4 h4,.df_adh_heading_4 h5,.df_adh_heading_4 h6,.df_adh_heading_4 h1 span,.df_adh_heading_4 h2 span,.df_adh_heading_4 h3 span,.df_adh_heading_4 h4 span,.df_adh_heading_4 h5 span,.df_adh_heading_4 h6 span{font-size:32px!important}.df_adh_heading_0 .df-heading-divider .df-divider-line::before,.df_adh_heading_1 .df-heading-divider .df-divider-line::before,.df_adh_heading_2 .df-heading-divider .df-divider-line::before,.df_adh_heading_3 .df-heading-divider .df-divider-line::before,.df_adh_heading_4 .df-heading-divider .df-divider-line::before{border-top-width:5px!important}.df_adh_heading_0 .df-heading-divider .df-divider-line,.df_adh_heading_1 .df-heading-divider .df-divider-line,.df_adh_heading_2 .df-heading-divider .df-divider-line,.df_adh_heading_3 .df-heading-divider .df-divider-line,.df_adh_heading_4 .df-heading-divider .df-divider-line{height:5px!important;border-radius:0px!important}.df_adh_heading_0 .df-heading-divider,.df_adh_heading_1 .df-heading-divider,.df_adh_heading_2 .df-heading-divider,.df_adh_heading_3 .df-heading-divider,.df_adh_heading_4 .df-heading-divider{max-width:60px!important}.df_adh_heading_0 .df-heading-divider .df-divider-line:before,.df_adh_heading_1 .df-heading-divider .df-divider-line:before,.df_adh_heading_2 .df-heading-divider .df-divider-line:before,.df_adh_heading_3 .df-heading-divider .df-divider-line:before,.df_adh_heading_4 .df-heading-divider .df-divider-line:before{border-radius:0px!important}.df_adh_heading_0 .df-heading-divider span,.df_adh_heading_1 .df-heading-divider span,.df_adh_heading_2 .df-heading-divider span,.df_adh_heading_3 .df-heading-divider span,.df_adh_heading_4 .df-heading-divider span{font-size:18px!important}.df_adh_heading_0 .df-heading-divider .et-pb-icon,.df_adh_heading_0 .df-heading-divider img,.df_adh_heading_1 .df-heading-divider .et-pb-icon,.df_adh_heading_1 .df-heading-divider img,.df_adh_heading_2 .df-heading-divider .et-pb-icon,.df_adh_heading_2 .df-heading-divider img,.df_adh_heading_3 .df-heading-divider .et-pb-icon,.df_adh_heading_3 .df-heading-divider img,.df_adh_heading_4 .df-heading-divider .et-pb-icon,.df_adh_heading_4 .df-heading-divider img{background-color:rgba(0,0,0,0)!important}.df_adh_heading_0 .df-heading-divider .divider-image,.df_adh_heading_1 .df-heading-divider .divider-image,.df_adh_heading_2 .df-heading-divider .divider-image,.df_adh_heading_3 .df-heading-divider .divider-image,.df_adh_heading_4 .df-heading-divider .divider-image{max-width:100px!important}.df_adh_heading_0 .df-heading .prefix,.df_adh_heading_0 .df-heading .infix,.df_adh_heading_0 .df-heading .suffix,.df_adh_heading_1 .df-heading .prefix,.df_adh_heading_1 .df-heading .infix,.df_adh_heading_1 .df-heading .suffix,.df_adh_heading_2 .df-heading .prefix,.df_adh_heading_2 .df-heading .infix,.df_adh_heading_2 .df-heading .suffix,.df_adh_heading_3 .df-heading .prefix,.df_adh_heading_3 .df-heading .infix,.df_adh_heading_3 .df-heading .suffix,.df_adh_heading_4 .df-heading .prefix,.df_adh_heading_4 .df-heading .infix,.df_adh_heading_4 .df-heading .suffix{display:inline-block;max-width:100%}.et_pb_image_2{width:70%}body #page-container .et_pb_section .et_pb_button_0:after{display:inline-block;opacity:0}body #page-container .et_pb_section .et_pb_button_0:hover:after{opacity:1}}</style>
  <!--copyscapeskip-->
  <button data-href="#moove_gdpr_cookie_modal" tabindex="1" id="moove_gdpr_save_popup_settings_button" style="display: none;" class="" aria-label="Change cookie settings">
    <span class="moove_gdpr_icon">
      <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" style="max-width: 30px; max-height: 30px;">
        <g data-name="1">
          <path d="M293.9,450H233.53a15,15,0,0,1-14.92-13.42l-4.47-42.09a152.77,152.77,0,0,1-18.25-7.56L163,413.53a15,15,0,0,1-20-1.06l-42.69-42.69a15,15,0,0,1-1.06-20l26.61-32.93a152.15,152.15,0,0,1-7.57-18.25L76.13,294.1a15,15,0,0,1-13.42-14.91V218.81A15,15,0,0,1,76.13,203.9l42.09-4.47a152.15,152.15,0,0,1,7.57-18.25L99.18,148.25a15,15,0,0,1,1.06-20l42.69-42.69a15,15,0,0,1,20-1.06l32.93,26.6a152.77,152.77,0,0,1,18.25-7.56l4.47-42.09A15,15,0,0,1,233.53,48H293.9a15,15,0,0,1,14.92,13.42l4.46,42.09a152.91,152.91,0,0,1,18.26,7.56l32.92-26.6a15,15,0,0,1,20,1.06l42.69,42.69a15,15,0,0,1,1.06,20l-26.61,32.93a153.8,153.8,0,0,1,7.57,18.25l42.09,4.47a15,15,0,0,1,13.41,14.91v60.38A15,15,0,0,1,451.3,294.1l-42.09,4.47a153.8,153.8,0,0,1-7.57,18.25l26.61,32.93a15,15,0,0,1-1.06,20L384.5,412.47a15,15,0,0,1-20,1.06l-32.92-26.6a152.91,152.91,0,0,1-18.26,7.56l-4.46,42.09A15,15,0,0,1,293.9,450ZM247,420h33.39l4.09-38.56a15,15,0,0,1,11.06-12.91A123,123,0,0,0,325.7,356a15,15,0,0,1,17,1.31l30.16,24.37,23.61-23.61L372.06,328a15,15,0,0,1-1.31-17,122.63,122.63,0,0,0,12.49-30.14,15,15,0,0,1,12.92-11.06l38.55-4.1V232.31l-38.55-4.1a15,15,0,0,1-12.92-11.06A122.63,122.63,0,0,0,370.75,187a15,15,0,0,1,1.31-17l24.37-30.16-23.61-23.61-30.16,24.37a15,15,0,0,1-17,1.31,123,123,0,0,0-30.14-12.49,15,15,0,0,1-11.06-12.91L280.41,78H247l-4.09,38.56a15,15,0,0,1-11.07,12.91A122.79,122.79,0,0,0,201.73,142a15,15,0,0,1-17-1.31L154.6,116.28,131,139.89l24.38,30.16a15,15,0,0,1,1.3,17,123.41,123.41,0,0,0-12.49,30.14,15,15,0,0,1-12.91,11.06l-38.56,4.1v33.38l38.56,4.1a15,15,0,0,1,12.91,11.06A123.41,123.41,0,0,0,156.67,311a15,15,0,0,1-1.3,17L131,358.11l23.61,23.61,30.17-24.37a15,15,0,0,1,17-1.31,122.79,122.79,0,0,0,30.13,12.49,15,15,0,0,1,11.07,12.91ZM449.71,279.19h0Z" fill="currentColor"></path>
          <path d="M263.71,340.36A91.36,91.36,0,1,1,355.08,249,91.46,91.46,0,0,1,263.71,340.36Zm0-152.72A61.36,61.36,0,1,0,325.08,249,61.43,61.43,0,0,0,263.71,187.64Z" fill="currentColor"></path>
        </g>
      </svg>
    </span>

    <span class="moove_gdpr_text">Change cookie settings</span>
  </button>
  <!--/copyscapeskip-->
    
  <!--copyscapeskip-->
  <!-- V1 -->
  <div id="moove_gdpr_cookie_modal" class="gdpr_lightbox-hide" role="complementary" aria-label="GDPR Settings Screen">
    <div class="moove-gdpr-modal-content moove-clearfix logo-position-left moove_gdpr_modal_theme_v1">
          
        <button class="moove-gdpr-modal-close" aria-label="Close GDPR Cookie Settings">
          <span class="gdpr-sr-only">Close GDPR Cookie Settings</span>
          <span class="gdpr-icon moovegdpr-arrow-close"></span>
        </button>
            <div class="moove-gdpr-modal-left-content">
        
<div class="moove-gdpr-company-logo-holder">
  <img data-src="https://www.empowersemi.com/wp-content/uploads/2025/01/EMPOWER-Color-Trimmed-300x73.png" alt="" width="300" height="73" class="img-responsive lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" style="--smush-placeholder-width: 300px; --smush-placeholder-aspect-ratio: 300/73;">
</div>
<!--  .moove-gdpr-company-logo-holder -->        <ul id="moove-gdpr-menu">
          
<li class="menu-item-on menu-item-privacy_overview menu-item-selected">
  <button data-href="#privacy_overview" class="moove-gdpr-tab-nav" aria-label="Privacy Overview">
    <span class="gdpr-nav-tab-title">Privacy Overview</span>
  </button>
</li>

  <li class="menu-item-strict-necessary-cookies menu-item-off">
    <button data-href="#strict-necessary-cookies" class="moove-gdpr-tab-nav" aria-label="Essential">
      <span class="gdpr-nav-tab-title">Essential</span>
    </button>
  </li>


  <li class="menu-item-off menu-item-third_party_cookies">
    <button data-href="#third_party_cookies" class="moove-gdpr-tab-nav" aria-label="Non-essential">
      <span class="gdpr-nav-tab-title">Non-essential</span>
    </button>
  </li>


        </ul>
        
<div class="moove-gdpr-branding-cnt">
  		<a href="https://wordpress.org/plugins/gdpr-cookie-compliance/" rel="noopener noreferrer" target="_blank" class="moove-gdpr-branding">Powered by&nbsp; <span>GDPR Cookie Compliance</span></a>
		</div>
<!--  .moove-gdpr-branding -->      </div>
      <!--  .moove-gdpr-modal-left-content -->
      <div class="moove-gdpr-modal-right-content">
        <div class="moove-gdpr-modal-title">
           
        </div>
        <!-- .moove-gdpr-modal-ritle -->
        <div class="main-modal-content">

          <div class="moove-gdpr-tab-content">
            
<div id="privacy_overview" class="moove-gdpr-tab-main">
      <span class="tab-title">Privacy Overview</span>
    <div class="moove-gdpr-tab-main-content">
  	<p>This website uses cookies so that we can provide you with the best
 user experience possible. Cookie information is stored in your browser 
and performs functions such as recognising you when you return to our 
website and helping our team to understand which sections of the website
 you find most interesting and useful. For more information please visit
 our <a href="https://www.empowersemi.com/privacy-policy">Privacy Policy</a></p>
  	  </div>
  <!--  .moove-gdpr-tab-main-content -->

</div>
<!-- #privacy_overview -->            
  <div id="strict-necessary-cookies" class="moove-gdpr-tab-main" style="display:none">
    <span class="tab-title">Essential</span>
    <div class="moove-gdpr-tab-main-content">
      <p>Essential Cookie should be enabled at all times so that we can save your preferences for cookie settings.</p>
      <div class="moove-gdpr-status-bar ">
        <div class="gdpr-cc-form-wrap">
          <div class="gdpr-cc-form-fieldset">
            <label class="cookie-switch" for="moove_gdpr_strict_cookies">    
              <span class="gdpr-sr-only">Enable or Disable Cookies</span>        
              <input type="checkbox" aria-label="Essential" value="check" name="moove_gdpr_strict_cookies" id="moove_gdpr_strict_cookies" checked="checked">
              <span class="cookie-slider cookie-round" data-text-enable="Enabled" data-text-disabled="Disabled"></span>
            </label>
          </div>
          <!-- .gdpr-cc-form-fieldset -->
        </div>
        <!-- .gdpr-cc-form-wrap -->
      </div>
      <!-- .moove-gdpr-status-bar -->
              <div class="moove-gdpr-strict-warning-message" style="margin-top: 10px;">
          <p>If you disable this cookie, we will not be able to save 
your preferences. This means that every time you visit this website you 
will need to enable or disable cookies again.</p>
        </div>
        <!--  .moove-gdpr-tab-main-content -->
                                              
    </div>
    <!--  .moove-gdpr-tab-main-content -->
  </div>
  <!-- #strict-necesarry-cookies -->
            
  <div id="third_party_cookies" class="moove-gdpr-tab-main" style="display:none">
    <span class="tab-title">Non-essential</span>
    <div class="moove-gdpr-tab-main-content">
      <p>This website uses Google Analytics and Leadfeeder to collect 
anonymous information such as the number of visitors to the site, and 
the most popular pages.<br>
Keeping this cookie enabled helps us to improve our website.</p>
      <div class="moove-gdpr-status-bar">
        <div class="gdpr-cc-form-wrap">
          <div class="gdpr-cc-form-fieldset">
            <label class="cookie-switch" for="moove_gdpr_performance_cookies">    
              <span class="gdpr-sr-only">Enable or Disable Cookies</span>     
              <input type="checkbox" aria-label="Non-essential" value="check" name="moove_gdpr_performance_cookies" id="moove_gdpr_performance_cookies" checked="checked">
              <span class="cookie-slider cookie-round" data-text-enable="Enabled" data-text-disabled="Disabled"></span>
            </label>
          </div>
          <!-- .gdpr-cc-form-fieldset -->
        </div>
        <!-- .gdpr-cc-form-wrap -->
      </div>
      <!-- .moove-gdpr-status-bar -->
              <div class="moove-gdpr-strict-secondary-warning-message" style="margin-top: 10px; display: none;">
          <p>Please enable Essential Cookies first so that we can save your preferences!</p>
        </div>
        <!--  .moove-gdpr-tab-main-content -->
             
    </div>
    <!--  .moove-gdpr-tab-main-content -->
  </div>
  <!-- #third_party_cookies -->
            
            
          </div>
          <!--  .moove-gdpr-tab-content -->
        </div>
        <!--  .main-modal-content -->
        <div class="moove-gdpr-modal-footer-content">
          <div class="moove-gdpr-button-holder">
			  		<button class="mgbutton moove-gdpr-modal-allow-all button-visible" aria-label="Enable All">Enable All</button>
		  					<button class="mgbutton moove-gdpr-modal-save-settings button-visible" aria-label="Save Settings">Save Settings</button>
				</div>
<!--  .moove-gdpr-button-holder -->        </div>
        <!--  .moove-gdpr-modal-footer-content -->
      </div>
      <!--  .moove-gdpr-modal-right-content -->

      <div class="moove-clearfix"></div>

    </div>
    <!--  .moove-gdpr-modal-content -->
  </div>
  <!-- #moove_gdpr_cookie_modal -->
  <!--/copyscapeskip-->
	
			<span class="et_pb_scroll_top et-pb-icon et-hidden" style="display: inline;"></span>
	

</body></html>'''
