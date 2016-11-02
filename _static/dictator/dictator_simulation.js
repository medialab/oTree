(function (lib, img, cjs, ss) {

var p; // shortcut to reference prototypes
lib.webFontTxtFilters = {}; 

// library properties:
lib.properties = {
	width: 600,
	height: 480,
	fps: 30,
	color: "#CCD1DB",
	opacity: 1.00,
	webfonts: {},
	manifest: []
};



lib.ssMetadata = [];


lib.webfontAvailable = function(family) { 
	lib.properties.webfonts[family] = true;
	var txtFilters = lib.webFontTxtFilters && lib.webFontTxtFilters[family] || [];
	for(var f = 0; f < txtFilters.length; ++f) {
		txtFilters[f].updateCache();
	}
};
// symbols:



(lib.portal_ray = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("rgba(0,204,255,0.31)").s().p("Ak4iyIJxkUIAAJxIpxEcg");
	this.shape.setTransform(31.4,45.6);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,62.7,91.1);


(lib.portal = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f().s("#686868").ss(0.5,0,0,4).p("AAzAAQAAAegPAUQgPAWgVAAQgUAAgPgWQgPgUAAgeQAAgdAPgVQAPgVAUAAQAVAAAPAVQAPAVAAAdg");
	this.shape.setTransform(5,-27.9);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f().s("#000000").ss(0.5,0,0,4).p("AFhFtIDmhnIAAuXQAAgWgNgLQgCgCgBAAQgOgKgTAKIvdG6QggAOgKAWQgHAPAAAgIAAOSIELh8IAAovQAAghAHgPQAKgTAggPIHPjOIAdgNQAVgLAPANQANALAAAWgAI3q0IAAgBIhPg0QgOgIgSAJIvdG6QggAOgKAWQgHAOAAAhIAAOVIBOAxAETjgIAAIdIBOAw");
	this.shape_1.setTransform(0,0.2);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#A3A3A3").s().p("Aofi/QAAghAHgPQALgVAfgPIPdm5QATgKAOAJIADACQANAMAAAVIAAOYIjmBmIAAo3QAAgVgMgMQgPgNgWALIgcANInQDPQgfAOgLAWQgGAMAAAhIAAIwIkMB7gAgnkwQAAAeAPAVQAPAWAUAAQAVAAAPgWQAPgVAAgeQAAgegPgVQgPgVgVAAQgUAAgPAVQgPAVAAAeIAAAAgAgYj9QgPgVAAgeQAAgeAPgVQAPgVAUAAQAVAAAPAVQAPAVAAAeQAAAegPAVQgPAWgVAAQgUAAgPgWgAA+kwIAAAAg");
	this.shape_2.setTransform(3.9,2.6);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#FFFFFF").s().p("Ao+K7IAAuUQAAghAHgPQAKgVAggPIPdm5QASgKAOAJIBPA0IAAAAQgOgJgTAKIvdG5QggAPgKAVQgHAPAAAhIAAORgAEbE/IAAoeIAdgNQAVgLAPANQANAMAAAVIAAI3g");
	this.shape_3.setTransform(-0.8,0);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(-59.3,-75.8,118.7,151.8);


(lib.participant_label = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.label = new cjs.Text("participant B", "bold 12px 'Gotham Bold'");
	this.label.name = "label";
	this.label.lineHeight = 13;
	this.label.lineWidth = 98;
	this.label.setTransform(16.6,2,1,1.213,0,66.7,32.2);

	this.timeline.addTween(cjs.Tween.get(this.label).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,103.4,61.7);


(lib.floor = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// mask (mask)
	var mask = new cjs.Shape();
	mask._off = true;
	mask.graphics.p("Egu3AlfMAAAhK9MBduAAAMAAABK9g");
	mask.setTransform(24.9,39.9);

	// grid
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape.setTransform(-1183.9,39.9,1.188,1.188);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_1.setTransform(-1160.2,39.9,1.188,1.188);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_2.setTransform(-1136.4,39.9,1.188,1.188);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_3.setTransform(-1112.6,39.9,1.188,1.188);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_4.setTransform(-1088.9,39.9,1.188,1.188);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_5.setTransform(-1065.1,39.9,1.188,1.188);

	this.shape_6 = new cjs.Shape();
	this.shape_6.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_6.setTransform(-1041.3,39.9,1.188,1.188);

	this.shape_7 = new cjs.Shape();
	this.shape_7.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_7.setTransform(-1017.6,39.9,1.188,1.188);

	this.shape_8 = new cjs.Shape();
	this.shape_8.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_8.setTransform(-993.8,39.9,1.188,1.188);

	this.shape_9 = new cjs.Shape();
	this.shape_9.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_9.setTransform(-970,39.9,1.188,1.188);

	this.shape_10 = new cjs.Shape();
	this.shape_10.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_10.setTransform(-946.3,39.9,1.188,1.188);

	this.shape_11 = new cjs.Shape();
	this.shape_11.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_11.setTransform(-922.5,39.9,1.188,1.188);

	this.shape_12 = new cjs.Shape();
	this.shape_12.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_12.setTransform(-898.7,39.9,1.188,1.188);

	this.shape_13 = new cjs.Shape();
	this.shape_13.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_13.setTransform(-875,39.9,1.188,1.188);

	this.shape_14 = new cjs.Shape();
	this.shape_14.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_14.setTransform(-851.2,39.9,1.188,1.188);

	this.shape_15 = new cjs.Shape();
	this.shape_15.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_15.setTransform(-827.4,39.9,1.188,1.188);

	this.shape_16 = new cjs.Shape();
	this.shape_16.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_16.setTransform(-803.7,39.9,1.188,1.188);

	this.shape_17 = new cjs.Shape();
	this.shape_17.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_17.setTransform(-779.9,39.9,1.188,1.188);

	this.shape_18 = new cjs.Shape();
	this.shape_18.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_18.setTransform(-756.2,39.9,1.188,1.188);

	this.shape_19 = new cjs.Shape();
	this.shape_19.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_19.setTransform(-732.4,39.9,1.188,1.188);

	this.shape_20 = new cjs.Shape();
	this.shape_20.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_20.setTransform(-708.6,39.9,1.188,1.188);

	this.shape_21 = new cjs.Shape();
	this.shape_21.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_21.setTransform(-684.9,39.9,1.188,1.188);

	this.shape_22 = new cjs.Shape();
	this.shape_22.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_22.setTransform(-661.1,39.9,1.188,1.188);

	this.shape_23 = new cjs.Shape();
	this.shape_23.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_23.setTransform(-637.3,39.9,1.188,1.188);

	this.shape_24 = new cjs.Shape();
	this.shape_24.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_24.setTransform(-613.6,39.9,1.188,1.188);

	this.shape_25 = new cjs.Shape();
	this.shape_25.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_25.setTransform(-589.8,39.9,1.188,1.188);

	this.shape_26 = new cjs.Shape();
	this.shape_26.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_26.setTransform(-566,39.9,1.188,1.188);

	this.shape_27 = new cjs.Shape();
	this.shape_27.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_27.setTransform(-542.3,39.9,1.188,1.188);

	this.shape_28 = new cjs.Shape();
	this.shape_28.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_28.setTransform(-518.5,39.9,1.188,1.188);

	this.shape_29 = new cjs.Shape();
	this.shape_29.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_29.setTransform(-494.7,39.9,1.188,1.188);

	this.shape_30 = new cjs.Shape();
	this.shape_30.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_30.setTransform(-471,39.9,1.188,1.188);

	this.shape_31 = new cjs.Shape();
	this.shape_31.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_31.setTransform(-447.2,39.9,1.188,1.188);

	this.shape_32 = new cjs.Shape();
	this.shape_32.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_32.setTransform(-423.4,39.9,1.188,1.188);

	this.shape_33 = new cjs.Shape();
	this.shape_33.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_33.setTransform(-399.7,39.9,1.188,1.188);

	this.shape_34 = new cjs.Shape();
	this.shape_34.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_34.setTransform(-375.9,39.9,1.188,1.188);

	this.shape_35 = new cjs.Shape();
	this.shape_35.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_35.setTransform(-352.1,39.9,1.188,1.188);

	this.shape_36 = new cjs.Shape();
	this.shape_36.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_36.setTransform(-328.4,39.9,1.188,1.188);

	this.shape_37 = new cjs.Shape();
	this.shape_37.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_37.setTransform(-304.6,39.9,1.188,1.188);

	this.shape_38 = new cjs.Shape();
	this.shape_38.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_38.setTransform(-280.8,39.9,1.188,1.188);

	this.shape_39 = new cjs.Shape();
	this.shape_39.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_39.setTransform(-257.1,39.9,1.188,1.188);

	this.shape_40 = new cjs.Shape();
	this.shape_40.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_40.setTransform(-233.3,39.9,1.188,1.188);

	this.shape_41 = new cjs.Shape();
	this.shape_41.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_41.setTransform(-209.5,39.9,1.188,1.188);

	this.shape_42 = new cjs.Shape();
	this.shape_42.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_42.setTransform(-185.8,39.9,1.188,1.188);

	this.shape_43 = new cjs.Shape();
	this.shape_43.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_43.setTransform(-162,39.9,1.188,1.188);

	this.shape_44 = new cjs.Shape();
	this.shape_44.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_44.setTransform(-138.2,39.9,1.188,1.188);

	this.shape_45 = new cjs.Shape();
	this.shape_45.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_45.setTransform(-114.5,39.9,1.188,1.188);

	this.shape_46 = new cjs.Shape();
	this.shape_46.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_46.setTransform(-90.7,39.9,1.188,1.188);

	this.shape_47 = new cjs.Shape();
	this.shape_47.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_47.setTransform(-66.9,39.9,1.188,1.188);

	this.shape_48 = new cjs.Shape();
	this.shape_48.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_48.setTransform(-43.2,39.9,1.188,1.188);

	this.shape_49 = new cjs.Shape();
	this.shape_49.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_49.setTransform(-19.4,39.9,1.188,1.188);

	this.shape_50 = new cjs.Shape();
	this.shape_50.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_50.setTransform(4.4,39.9,1.188,1.188);

	this.shape_51 = new cjs.Shape();
	this.shape_51.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_51.setTransform(28.1,39.9,1.188,1.188);

	this.shape_52 = new cjs.Shape();
	this.shape_52.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_52.setTransform(51.9,39.9,1.188,1.188);

	this.shape_53 = new cjs.Shape();
	this.shape_53.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_53.setTransform(75.7,39.9,1.188,1.188);

	this.shape_54 = new cjs.Shape();
	this.shape_54.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_54.setTransform(-1018,43.1,1.188,1.188);

	this.shape_55 = new cjs.Shape();
	this.shape_55.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_55.setTransform(-994.2,43.1,1.188,1.188);

	this.shape_56 = new cjs.Shape();
	this.shape_56.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_56.setTransform(-970.5,43.1,1.188,1.188);

	this.shape_57 = new cjs.Shape();
	this.shape_57.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_57.setTransform(-946.7,43.1,1.188,1.188);

	this.shape_58 = new cjs.Shape();
	this.shape_58.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_58.setTransform(-923,43.1,1.188,1.188);

	this.shape_59 = new cjs.Shape();
	this.shape_59.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_59.setTransform(-899.2,43.1,1.188,1.188);

	this.shape_60 = new cjs.Shape();
	this.shape_60.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_60.setTransform(-875.4,43.1,1.188,1.188);

	this.shape_61 = new cjs.Shape();
	this.shape_61.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_61.setTransform(-851.7,43.1,1.188,1.188);

	this.shape_62 = new cjs.Shape();
	this.shape_62.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_62.setTransform(-827.9,43.1,1.188,1.188);

	this.shape_63 = new cjs.Shape();
	this.shape_63.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_63.setTransform(-804.1,43.1,1.188,1.188);

	this.shape_64 = new cjs.Shape();
	this.shape_64.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_64.setTransform(-780.4,43.1,1.188,1.188);

	this.shape_65 = new cjs.Shape();
	this.shape_65.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_65.setTransform(-756.6,43.1,1.188,1.188);

	this.shape_66 = new cjs.Shape();
	this.shape_66.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_66.setTransform(-732.8,43.1,1.188,1.188);

	this.shape_67 = new cjs.Shape();
	this.shape_67.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_67.setTransform(-709.1,43.1,1.188,1.188);

	this.shape_68 = new cjs.Shape();
	this.shape_68.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_68.setTransform(-685.3,43.1,1.188,1.188);

	this.shape_69 = new cjs.Shape();
	this.shape_69.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_69.setTransform(-661.5,43.1,1.188,1.188);

	this.shape_70 = new cjs.Shape();
	this.shape_70.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_70.setTransform(-637.8,43.1,1.188,1.188);

	this.shape_71 = new cjs.Shape();
	this.shape_71.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_71.setTransform(-614,43.1,1.188,1.188);

	this.shape_72 = new cjs.Shape();
	this.shape_72.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_72.setTransform(-590.2,43.1,1.188,1.188);

	this.shape_73 = new cjs.Shape();
	this.shape_73.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_73.setTransform(-566.5,43.1,1.188,1.188);

	this.shape_74 = new cjs.Shape();
	this.shape_74.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_74.setTransform(-542.7,43.1,1.188,1.188);

	this.shape_75 = new cjs.Shape();
	this.shape_75.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_75.setTransform(-518.9,43.1,1.188,1.188);

	this.shape_76 = new cjs.Shape();
	this.shape_76.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_76.setTransform(-495.2,43.1,1.188,1.188);

	this.shape_77 = new cjs.Shape();
	this.shape_77.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_77.setTransform(-471.4,43.1,1.188,1.188);

	this.shape_78 = new cjs.Shape();
	this.shape_78.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_78.setTransform(-447.6,43.1,1.188,1.188);

	this.shape_79 = new cjs.Shape();
	this.shape_79.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_79.setTransform(-423.9,43.1,1.188,1.188);

	this.shape_80 = new cjs.Shape();
	this.shape_80.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_80.setTransform(-400.1,43.1,1.188,1.188);

	this.shape_81 = new cjs.Shape();
	this.shape_81.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_81.setTransform(-376.3,43.1,1.188,1.188);

	this.shape_82 = new cjs.Shape();
	this.shape_82.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_82.setTransform(-352.6,43.1,1.188,1.188);

	this.shape_83 = new cjs.Shape();
	this.shape_83.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_83.setTransform(-328.8,43.1,1.188,1.188);

	this.shape_84 = new cjs.Shape();
	this.shape_84.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_84.setTransform(-305,43.1,1.188,1.188);

	this.shape_85 = new cjs.Shape();
	this.shape_85.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_85.setTransform(-281.3,43.1,1.188,1.188);

	this.shape_86 = new cjs.Shape();
	this.shape_86.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_86.setTransform(-257.5,43.1,1.188,1.188);

	this.shape_87 = new cjs.Shape();
	this.shape_87.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_87.setTransform(-233.7,43.1,1.188,1.188);

	this.shape_88 = new cjs.Shape();
	this.shape_88.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_88.setTransform(-210,43.1,1.188,1.188);

	this.shape_89 = new cjs.Shape();
	this.shape_89.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_89.setTransform(-186.2,43.1,1.188,1.188);

	this.shape_90 = new cjs.Shape();
	this.shape_90.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_90.setTransform(-162.4,43.1,1.188,1.188);

	this.shape_91 = new cjs.Shape();
	this.shape_91.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_91.setTransform(-138.7,43.1,1.188,1.188);

	this.shape_92 = new cjs.Shape();
	this.shape_92.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_92.setTransform(-114.9,43.1,1.188,1.188);

	this.shape_93 = new cjs.Shape();
	this.shape_93.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_93.setTransform(-91.1,43.1,1.188,1.188);

	this.shape_94 = new cjs.Shape();
	this.shape_94.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_94.setTransform(99.4,39.9,1.188,1.188);

	this.shape_95 = new cjs.Shape();
	this.shape_95.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_95.setTransform(123.2,39.9,1.188,1.188);

	this.shape_96 = new cjs.Shape();
	this.shape_96.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_96.setTransform(147,39.9,1.188,1.188);

	this.shape_97 = new cjs.Shape();
	this.shape_97.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_97.setTransform(170.7,39.9,1.188,1.188);

	this.shape_98 = new cjs.Shape();
	this.shape_98.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_98.setTransform(194.5,39.9,1.188,1.188);

	this.shape_99 = new cjs.Shape();
	this.shape_99.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_99.setTransform(218.3,39.9,1.188,1.188);

	this.shape_100 = new cjs.Shape();
	this.shape_100.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_100.setTransform(242,39.9,1.188,1.188);

	this.shape_101 = new cjs.Shape();
	this.shape_101.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_101.setTransform(265.8,39.9,1.188,1.188);

	this.shape_102 = new cjs.Shape();
	this.shape_102.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_102.setTransform(289.6,39.9,1.188,1.188);

	this.shape_103 = new cjs.Shape();
	this.shape_103.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_103.setTransform(313.3,39.9,1.188,1.188);

	this.shape_104 = new cjs.Shape();
	this.shape_104.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_104.setTransform(337.1,39.9,1.188,1.188);

	this.shape_105 = new cjs.Shape();
	this.shape_105.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_105.setTransform(360.9,39.9,1.188,1.188);

	this.shape_106 = new cjs.Shape();
	this.shape_106.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_106.setTransform(384.7,39.9,1.188,1.188);

	this.shape_107 = new cjs.Shape();
	this.shape_107.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_107.setTransform(408.4,39.9,1.188,1.188);

	this.shape_108 = new cjs.Shape();
	this.shape_108.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_108.setTransform(432.2,39.9,1.188,1.188);

	this.shape_109 = new cjs.Shape();
	this.shape_109.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_109.setTransform(456,39.9,1.188,1.188);

	this.shape_110 = new cjs.Shape();
	this.shape_110.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_110.setTransform(479.7,39.9,1.188,1.188);

	this.shape_111 = new cjs.Shape();
	this.shape_111.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_111.setTransform(503.5,39.9,1.188,1.188);

	this.shape_112 = new cjs.Shape();
	this.shape_112.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_112.setTransform(527.3,39.9,1.188,1.188);

	this.shape_113 = new cjs.Shape();
	this.shape_113.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_113.setTransform(551,39.9,1.188,1.188);

	this.shape_114 = new cjs.Shape();
	this.shape_114.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_114.setTransform(574.8,39.9,1.188,1.188);

	this.shape_115 = new cjs.Shape();
	this.shape_115.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_115.setTransform(598.6,39.9,1.188,1.188);

	this.shape_116 = new cjs.Shape();
	this.shape_116.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_116.setTransform(622.3,39.9,1.188,1.188);

	this.shape_117 = new cjs.Shape();
	this.shape_117.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_117.setTransform(646.1,39.9,1.188,1.188);

	this.shape_118 = new cjs.Shape();
	this.shape_118.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_118.setTransform(669.9,39.9,1.188,1.188);

	this.shape_119 = new cjs.Shape();
	this.shape_119.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_119.setTransform(693.6,39.9,1.188,1.188);

	this.shape_120 = new cjs.Shape();
	this.shape_120.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_120.setTransform(717.4,39.9,1.188,1.188);

	this.shape_121 = new cjs.Shape();
	this.shape_121.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_121.setTransform(741.2,39.9,1.188,1.188);

	this.shape_122 = new cjs.Shape();
	this.shape_122.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_122.setTransform(764.9,39.9,1.188,1.188);

	this.shape_123 = new cjs.Shape();
	this.shape_123.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_123.setTransform(788.7,39.9,1.188,1.188);

	this.shape_124 = new cjs.Shape();
	this.shape_124.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_124.setTransform(812.5,39.9,1.188,1.188);

	this.shape_125 = new cjs.Shape();
	this.shape_125.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_125.setTransform(836.2,39.9,1.188,1.188);

	this.shape_126 = new cjs.Shape();
	this.shape_126.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_126.setTransform(860,39.9,1.188,1.188);

	this.shape_127 = new cjs.Shape();
	this.shape_127.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_127.setTransform(883.8,39.9,1.188,1.188);

	this.shape_128 = new cjs.Shape();
	this.shape_128.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_128.setTransform(907.5,39.9,1.188,1.188);

	this.shape_129 = new cjs.Shape();
	this.shape_129.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_129.setTransform(931.3,39.9,1.188,1.188);

	this.shape_130 = new cjs.Shape();
	this.shape_130.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_130.setTransform(955.1,39.9,1.188,1.188);

	this.shape_131 = new cjs.Shape();
	this.shape_131.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_131.setTransform(978.8,39.9,1.188,1.188);

	this.shape_132 = new cjs.Shape();
	this.shape_132.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_132.setTransform(1002.6,39.9,1.188,1.188);

	this.shape_133 = new cjs.Shape();
	this.shape_133.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_133.setTransform(1026.4,39.9,1.188,1.188);

	this.shape_134 = new cjs.Shape();
	this.shape_134.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_134.setTransform(1050.1,39.9,1.188,1.188);

	this.shape_135 = new cjs.Shape();
	this.shape_135.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_135.setTransform(1073.9,39.9,1.188,1.188);

	this.shape_136 = new cjs.Shape();
	this.shape_136.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_136.setTransform(1097.7,39.9,1.188,1.188);

	this.shape_137 = new cjs.Shape();
	this.shape_137.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_137.setTransform(1121.4,39.9,1.188,1.188);

	this.shape_138 = new cjs.Shape();
	this.shape_138.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_138.setTransform(1145.2,39.9,1.188,1.188);

	this.shape_139 = new cjs.Shape();
	this.shape_139.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_139.setTransform(1169,39.9,1.188,1.188);

	this.shape_140 = new cjs.Shape();
	this.shape_140.graphics.f("#000000").s().p("EhKMAhEMCUYhCJIABACMiUYBCJg");
	this.shape_140.setTransform(1192.7,39.9,1.188,1.188);

	this.shape_141 = new cjs.Shape();
	this.shape_141.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_141.setTransform(-67.4,43.1,1.188,1.188);

	this.shape_142 = new cjs.Shape();
	this.shape_142.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_142.setTransform(-43.6,43.1,1.188,1.188);

	this.shape_143 = new cjs.Shape();
	this.shape_143.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_143.setTransform(-19.8,43.1,1.188,1.188);

	this.shape_144 = new cjs.Shape();
	this.shape_144.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_144.setTransform(3.9,43.1,1.188,1.188);

	this.shape_145 = new cjs.Shape();
	this.shape_145.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_145.setTransform(27.7,43.1,1.188,1.188);

	this.shape_146 = new cjs.Shape();
	this.shape_146.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_146.setTransform(51.5,43.1,1.188,1.188);

	this.shape_147 = new cjs.Shape();
	this.shape_147.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_147.setTransform(75.2,43.1,1.188,1.188);

	this.shape_148 = new cjs.Shape();
	this.shape_148.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_148.setTransform(99,43.1,1.188,1.188);

	this.shape_149 = new cjs.Shape();
	this.shape_149.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_149.setTransform(122.8,43.1,1.188,1.188);

	this.shape_150 = new cjs.Shape();
	this.shape_150.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_150.setTransform(146.5,43.1,1.188,1.188);

	this.shape_151 = new cjs.Shape();
	this.shape_151.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_151.setTransform(170.3,43.1,1.188,1.188);

	this.shape_152 = new cjs.Shape();
	this.shape_152.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_152.setTransform(194.1,43.1,1.188,1.188);

	this.shape_153 = new cjs.Shape();
	this.shape_153.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_153.setTransform(217.8,43.1,1.188,1.188);

	this.shape_154 = new cjs.Shape();
	this.shape_154.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_154.setTransform(241.6,43.1,1.188,1.188);

	this.shape_155 = new cjs.Shape();
	this.shape_155.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_155.setTransform(265.4,43.1,1.188,1.188);

	this.shape_156 = new cjs.Shape();
	this.shape_156.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_156.setTransform(289.1,43.1,1.188,1.188);

	this.shape_157 = new cjs.Shape();
	this.shape_157.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_157.setTransform(312.9,43.1,1.188,1.188);

	this.shape_158 = new cjs.Shape();
	this.shape_158.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_158.setTransform(336.7,43.1,1.188,1.188);

	this.shape_159 = new cjs.Shape();
	this.shape_159.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_159.setTransform(360.4,43.1,1.188,1.188);

	this.shape_160 = new cjs.Shape();
	this.shape_160.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_160.setTransform(384.2,43.1,1.188,1.188);

	this.shape_161 = new cjs.Shape();
	this.shape_161.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_161.setTransform(408,43.1,1.188,1.188);

	this.shape_162 = new cjs.Shape();
	this.shape_162.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_162.setTransform(431.7,43.1,1.188,1.188);

	this.shape_163 = new cjs.Shape();
	this.shape_163.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_163.setTransform(455.5,43.1,1.188,1.188);

	this.shape_164 = new cjs.Shape();
	this.shape_164.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_164.setTransform(479.3,43.1,1.188,1.188);

	this.shape_165 = new cjs.Shape();
	this.shape_165.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_165.setTransform(503,43.1,1.188,1.188);

	this.shape_166 = new cjs.Shape();
	this.shape_166.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_166.setTransform(526.8,43.1,1.188,1.188);

	this.shape_167 = new cjs.Shape();
	this.shape_167.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_167.setTransform(550.6,43.1,1.188,1.188);

	this.shape_168 = new cjs.Shape();
	this.shape_168.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_168.setTransform(574.3,43.1,1.188,1.188);

	this.shape_169 = new cjs.Shape();
	this.shape_169.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_169.setTransform(598.1,43.1,1.188,1.188);

	this.shape_170 = new cjs.Shape();
	this.shape_170.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_170.setTransform(621.9,43.1,1.188,1.188);

	this.shape_171 = new cjs.Shape();
	this.shape_171.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_171.setTransform(645.6,43.1,1.188,1.188);

	this.shape_172 = new cjs.Shape();
	this.shape_172.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_172.setTransform(669.4,43.1,1.188,1.188);

	this.shape_173 = new cjs.Shape();
	this.shape_173.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_173.setTransform(693.2,43.1,1.188,1.188);

	this.shape_174 = new cjs.Shape();
	this.shape_174.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_174.setTransform(716.9,43.1,1.188,1.188);

	this.shape_175 = new cjs.Shape();
	this.shape_175.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_175.setTransform(740.7,43.1,1.188,1.188);

	this.shape_176 = new cjs.Shape();
	this.shape_176.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_176.setTransform(764.5,43.1,1.188,1.188);

	this.shape_177 = new cjs.Shape();
	this.shape_177.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_177.setTransform(788.2,43.1,1.188,1.188);

	this.shape_178 = new cjs.Shape();
	this.shape_178.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_178.setTransform(812,43.1,1.188,1.188);

	this.shape_179 = new cjs.Shape();
	this.shape_179.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_179.setTransform(835.8,43.1,1.188,1.188);

	this.shape_180 = new cjs.Shape();
	this.shape_180.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_180.setTransform(859.5,43.1,1.188,1.188);

	this.shape_181 = new cjs.Shape();
	this.shape_181.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_181.setTransform(883.3,43.1,1.188,1.188);

	this.shape_182 = new cjs.Shape();
	this.shape_182.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_182.setTransform(907.1,43.1,1.188,1.188);

	this.shape_183 = new cjs.Shape();
	this.shape_183.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_183.setTransform(930.8,43.1,1.188,1.188);

	this.shape_184 = new cjs.Shape();
	this.shape_184.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_184.setTransform(954.6,43.1,1.188,1.188);

	this.shape_185 = new cjs.Shape();
	this.shape_185.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_185.setTransform(978.4,43.1,1.188,1.188);

	this.shape_186 = new cjs.Shape();
	this.shape_186.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_186.setTransform(1002.1,43.1,1.188,1.188);

	this.shape_187 = new cjs.Shape();
	this.shape_187.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_187.setTransform(1025.9,43.1,1.188,1.188);

	this.shape_188 = new cjs.Shape();
	this.shape_188.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_188.setTransform(1049.7,43.1,1.188,1.188);

	this.shape_189 = new cjs.Shape();
	this.shape_189.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_189.setTransform(1073.4,43.1,1.188,1.188);

	this.shape_190 = new cjs.Shape();
	this.shape_190.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_190.setTransform(1097.2,43.1,1.188,1.188);

	this.shape_191 = new cjs.Shape();
	this.shape_191.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_191.setTransform(1121,43.1,1.188,1.188);

	this.shape_192 = new cjs.Shape();
	this.shape_192.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_192.setTransform(1144.7,43.1,1.188,1.188);

	this.shape_193 = new cjs.Shape();
	this.shape_193.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_193.setTransform(1168.5,43.1,1.188,1.188);

	this.shape_194 = new cjs.Shape();
	this.shape_194.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_194.setTransform(1192.3,43.1,1.188,1.188);

	this.shape_195 = new cjs.Shape();
	this.shape_195.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_195.setTransform(1216,43.1,1.188,1.188);

	this.shape_196 = new cjs.Shape();
	this.shape_196.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_196.setTransform(1239.8,43.1,1.188,1.188);

	this.shape_197 = new cjs.Shape();
	this.shape_197.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_197.setTransform(1263.6,43.1,1.188,1.188);

	this.shape_198 = new cjs.Shape();
	this.shape_198.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_198.setTransform(1287.3,43.1,1.188,1.188);

	this.shape_199 = new cjs.Shape();
	this.shape_199.graphics.f("#000000").s().p("Eg0DggpIACgCMBoFBBVIgBACg");
	this.shape_199.setTransform(1311.1,43.1,1.188,1.188);

	this.shape_200 = new cjs.Shape();
	this.shape_200.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_200.setTransform(1334.9,43.1,1.188,1.188);

	this.shape_201 = new cjs.Shape();
	this.shape_201.graphics.f("#000000").s().p("Eg0DggpIABgCMBoGBBVIgBACg");
	this.shape_201.setTransform(1358.6,43.1,1.188,1.188);

	this.shape.mask = this.shape_1.mask = this.shape_2.mask = this.shape_3.mask = this.shape_4.mask = this.shape_5.mask = this.shape_6.mask = this.shape_7.mask = this.shape_8.mask = this.shape_9.mask = this.shape_10.mask = this.shape_11.mask = this.shape_12.mask = this.shape_13.mask = this.shape_14.mask = this.shape_15.mask = this.shape_16.mask = this.shape_17.mask = this.shape_18.mask = this.shape_19.mask = this.shape_20.mask = this.shape_21.mask = this.shape_22.mask = this.shape_23.mask = this.shape_24.mask = this.shape_25.mask = this.shape_26.mask = this.shape_27.mask = this.shape_28.mask = this.shape_29.mask = this.shape_30.mask = this.shape_31.mask = this.shape_32.mask = this.shape_33.mask = this.shape_34.mask = this.shape_35.mask = this.shape_36.mask = this.shape_37.mask = this.shape_38.mask = this.shape_39.mask = this.shape_40.mask = this.shape_41.mask = this.shape_42.mask = this.shape_43.mask = this.shape_44.mask = this.shape_45.mask = this.shape_46.mask = this.shape_47.mask = this.shape_48.mask = this.shape_49.mask = this.shape_50.mask = this.shape_51.mask = this.shape_52.mask = this.shape_53.mask = this.shape_54.mask = this.shape_55.mask = this.shape_56.mask = this.shape_57.mask = this.shape_58.mask = this.shape_59.mask = this.shape_60.mask = this.shape_61.mask = this.shape_62.mask = this.shape_63.mask = this.shape_64.mask = this.shape_65.mask = this.shape_66.mask = this.shape_67.mask = this.shape_68.mask = this.shape_69.mask = this.shape_70.mask = this.shape_71.mask = this.shape_72.mask = this.shape_73.mask = this.shape_74.mask = this.shape_75.mask = this.shape_76.mask = this.shape_77.mask = this.shape_78.mask = this.shape_79.mask = this.shape_80.mask = this.shape_81.mask = this.shape_82.mask = this.shape_83.mask = this.shape_84.mask = this.shape_85.mask = this.shape_86.mask = this.shape_87.mask = this.shape_88.mask = this.shape_89.mask = this.shape_90.mask = this.shape_91.mask = this.shape_92.mask = this.shape_93.mask = this.shape_94.mask = this.shape_95.mask = this.shape_96.mask = this.shape_97.mask = this.shape_98.mask = this.shape_99.mask = this.shape_100.mask = this.shape_101.mask = this.shape_102.mask = this.shape_103.mask = this.shape_104.mask = this.shape_105.mask = this.shape_106.mask = this.shape_107.mask = this.shape_108.mask = this.shape_109.mask = this.shape_110.mask = this.shape_111.mask = this.shape_112.mask = this.shape_113.mask = this.shape_114.mask = this.shape_115.mask = this.shape_116.mask = this.shape_117.mask = this.shape_118.mask = this.shape_119.mask = this.shape_120.mask = this.shape_121.mask = this.shape_122.mask = this.shape_123.mask = this.shape_124.mask = this.shape_125.mask = this.shape_126.mask = this.shape_127.mask = this.shape_128.mask = this.shape_129.mask = this.shape_130.mask = this.shape_131.mask = this.shape_132.mask = this.shape_133.mask = this.shape_134.mask = this.shape_135.mask = this.shape_136.mask = this.shape_137.mask = this.shape_138.mask = this.shape_139.mask = this.shape_140.mask = this.shape_141.mask = this.shape_142.mask = this.shape_143.mask = this.shape_144.mask = this.shape_145.mask = this.shape_146.mask = this.shape_147.mask = this.shape_148.mask = this.shape_149.mask = this.shape_150.mask = this.shape_151.mask = this.shape_152.mask = this.shape_153.mask = this.shape_154.mask = this.shape_155.mask = this.shape_156.mask = this.shape_157.mask = this.shape_158.mask = this.shape_159.mask = this.shape_160.mask = this.shape_161.mask = this.shape_162.mask = this.shape_163.mask = this.shape_164.mask = this.shape_165.mask = this.shape_166.mask = this.shape_167.mask = this.shape_168.mask = this.shape_169.mask = this.shape_170.mask = this.shape_171.mask = this.shape_172.mask = this.shape_173.mask = this.shape_174.mask = this.shape_175.mask = this.shape_176.mask = this.shape_177.mask = this.shape_178.mask = this.shape_179.mask = this.shape_180.mask = this.shape_181.mask = this.shape_182.mask = this.shape_183.mask = this.shape_184.mask = this.shape_185.mask = this.shape_186.mask = this.shape_187.mask = this.shape_188.mask = this.shape_189.mask = this.shape_190.mask = this.shape_191.mask = this.shape_192.mask = this.shape_193.mask = this.shape_194.mask = this.shape_195.mask = this.shape_196.mask = this.shape_197.mask = this.shape_198.mask = this.shape_199.mask = this.shape_200.mask = this.shape_201.mask = mask;

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_201},{t:this.shape_200},{t:this.shape_199},{t:this.shape_198},{t:this.shape_197},{t:this.shape_196},{t:this.shape_195},{t:this.shape_194},{t:this.shape_193},{t:this.shape_192},{t:this.shape_191},{t:this.shape_190},{t:this.shape_189},{t:this.shape_188},{t:this.shape_187},{t:this.shape_186},{t:this.shape_185},{t:this.shape_184},{t:this.shape_183},{t:this.shape_182},{t:this.shape_181},{t:this.shape_180},{t:this.shape_179},{t:this.shape_178},{t:this.shape_177},{t:this.shape_176},{t:this.shape_175},{t:this.shape_174},{t:this.shape_173},{t:this.shape_172},{t:this.shape_171},{t:this.shape_170},{t:this.shape_169},{t:this.shape_168},{t:this.shape_167},{t:this.shape_166},{t:this.shape_165},{t:this.shape_164},{t:this.shape_163},{t:this.shape_162},{t:this.shape_161},{t:this.shape_160},{t:this.shape_159},{t:this.shape_158},{t:this.shape_157},{t:this.shape_156},{t:this.shape_155},{t:this.shape_154},{t:this.shape_153},{t:this.shape_152},{t:this.shape_151},{t:this.shape_150},{t:this.shape_149},{t:this.shape_148},{t:this.shape_147},{t:this.shape_146},{t:this.shape_145},{t:this.shape_144},{t:this.shape_143},{t:this.shape_142},{t:this.shape_141},{t:this.shape_140},{t:this.shape_139},{t:this.shape_138},{t:this.shape_137},{t:this.shape_136},{t:this.shape_135},{t:this.shape_134},{t:this.shape_133},{t:this.shape_132},{t:this.shape_131},{t:this.shape_130},{t:this.shape_129},{t:this.shape_128},{t:this.shape_127},{t:this.shape_126},{t:this.shape_125},{t:this.shape_124},{t:this.shape_123},{t:this.shape_122},{t:this.shape_121},{t:this.shape_120},{t:this.shape_119},{t:this.shape_118},{t:this.shape_117},{t:this.shape_116},{t:this.shape_115},{t:this.shape_114},{t:this.shape_113},{t:this.shape_112},{t:this.shape_111},{t:this.shape_110},{t:this.shape_109},{t:this.shape_108},{t:this.shape_107},{t:this.shape_106},{t:this.shape_105},{t:this.shape_104},{t:this.shape_103},{t:this.shape_102},{t:this.shape_101},{t:this.shape_100},{t:this.shape_99},{t:this.shape_98},{t:this.shape_97},{t:this.shape_96},{t:this.shape_95},{t:this.shape_94},{t:this.shape_93},{t:this.shape_92},{t:this.shape_91},{t:this.shape_90},{t:this.shape_89},{t:this.shape_88},{t:this.shape_87},{t:this.shape_86},{t:this.shape_85},{t:this.shape_84},{t:this.shape_83},{t:this.shape_82},{t:this.shape_81},{t:this.shape_80},{t:this.shape_79},{t:this.shape_78},{t:this.shape_77},{t:this.shape_76},{t:this.shape_75},{t:this.shape_74},{t:this.shape_73},{t:this.shape_72},{t:this.shape_71},{t:this.shape_70},{t:this.shape_69},{t:this.shape_68},{t:this.shape_67},{t:this.shape_66},{t:this.shape_65},{t:this.shape_64},{t:this.shape_63},{t:this.shape_62},{t:this.shape_61},{t:this.shape_60},{t:this.shape_59},{t:this.shape_58},{t:this.shape_57},{t:this.shape_56},{t:this.shape_55},{t:this.shape_54},{t:this.shape_53},{t:this.shape_52},{t:this.shape_51},{t:this.shape_50},{t:this.shape_49},{t:this.shape_48},{t:this.shape_47},{t:this.shape_46},{t:this.shape_45},{t:this.shape_44},{t:this.shape_43},{t:this.shape_42},{t:this.shape_41},{t:this.shape_40},{t:this.shape_39},{t:this.shape_38},{t:this.shape_37},{t:this.shape_36},{t:this.shape_35},{t:this.shape_34},{t:this.shape_33},{t:this.shape_32},{t:this.shape_31},{t:this.shape_30},{t:this.shape_29},{t:this.shape_28},{t:this.shape_27},{t:this.shape_26},{t:this.shape_25},{t:this.shape_24},{t:this.shape_23},{t:this.shape_22},{t:this.shape_21},{t:this.shape_20},{t:this.shape_19},{t:this.shape_18},{t:this.shape_17},{t:this.shape_16},{t:this.shape_15},{t:this.shape_14},{t:this.shape_13},{t:this.shape_12},{t:this.shape_11},{t:this.shape_10},{t:this.shape_9},{t:this.shape_8},{t:this.shape_7},{t:this.shape_6},{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(-275.1,-200.1,600,480);


(lib.dollarsGrey = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#313131").s().p("AhvALICWhDIBJAuIiWBDgAhhALIA8AmIAAAAICHg8Ig8glg");
	this.shape.setTransform(12.1,6.2);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#6A6A6A").s().p("Ah3AKICehGIBRAzIieBGgAhvALIBKAuICVhDIhJgugAhhAMICHg8IA9AlIiIA8IAAABgAADAKIgMAGIAHAFIAMgGIAHADIAAAAIAGgCIACgBIgHgEIAIgEIgHgDIAIgEIgIgCIgHACIgGgDIgGADIgHgEIAOgHIgHgEIAAAAIgNAHIgHgEIAAAAIgHADIAGAEIgHADIAGACIgHAEIAHAEIAHgDIAHAEIAIgDgAAFADIAHgDIAGADIgHADgAgVABIAAgBIAHgBIAHADIgIADg");
	this.shape_1.setTransform(12.1,6.2);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#FFFFFF").s().p("AgHAOIAMgHIgFgDIgGADIgHgFIgHAEIgHgFIAHgBIgGgEIAHgEIgHgDIAIgEIAAAAIAHAFIAMgIIABABIAGAEIgNAGIAFAFIAHgEIAHAFIAHgEIAHAFIgHABIAGAEIgHADIAHAFIgCAAIgGADIAAAAIgHgEIgMAGgAAHAAIAGAEIAHgEIgGgBgAgTAAIAAAAIAGACIAHgCIgGgDg");
	this.shape_2.setTransform(11.9,6.4);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,24.1,12.3);


(lib.dollarsGreen = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#628118").s().p("AhvALICWhDIBJAuIiWBDgAhhALIA8AmICHg8Ig8glg");
	this.shape.setTransform(12.1,6.2);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#FFFFFF").s().p("AgHAOIANgHIgGgDIgGADIgHgFIgHAEIgHgFIAHgBIgGgEIAHgEIgHgDIAIgEIAHAFIANgIIAGAFIgMAGIAEAFIAHgEIAHAFIAHgEIAHAFIgHABIAHAEIgIADIAHAFIgIADIgHgEIgMAGgAAHAAIAGAEIAHgEIgGgBgAgTAAIAGACIAHgCIgGgDg");
	this.shape_1.setTransform(11.9,6.4);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#93AD3F").s().p("Ah3AKICehGIBRAzIieBGgAhvALIBKAuICVhDIhJgugAhhAMICHg8IA9AlIiHA9gAAEAKIgNAGIAHAFIAMgGIAIADIAHgDIgHgEIAIgEIgHgDIAIgEIgIgCIgHACIgGgDIgGADIgGgEIANgHIgHgEIgNAHIgGgEIgIADIAGAEIgHADIAGADIgHADIAHAEIAHgDIAHAEIAIgDgAAFADIAHgDIAGADIgHADgAgVABIAHgCIAHADIgIADg");
	this.shape_2.setTransform(12.1,6.2);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,24.1,12.3);


(lib.conveyor = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("rgba(163,163,163,0.902)").s().p("A/yvCICNAZIgXhOICOAZIgahOIABAAICSAYIgehMICRAXIgdhLICPAYIgdhLMA2gAiMIpHEDg");
	this.shape.setTransform(-4.3,-2.7);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#474747").s().p("AV/SuIACgBIJHkEIBWA2IpGEFgEggdgPeIDqhpIAAAAIAaBNIiOgZIAXBPgA8yxHIB0g1IAeBMgA6+x8IB0g0IBygzIAdBMIiPgZIAdBMg");

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(-207.8,-125.2,415.7,250.5);


(lib.character = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#000000").s().p("AgPAAIAAgSIAfASIAAATg");
	this.shape.setTransform(7.7,52.9);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#000000").s().p("AgPAAIAAgSIAfASIAAATg");
	this.shape_1.setTransform(1.7,49.3);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#000000").s().p("AgNApIAChhIAZAQIgCBhg");
	this.shape_2.setTransform(5.6,7.7);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#000000").s().p("AgGA3IACh1IALAIIgCB0g");
	this.shape_3.setTransform(6.8,45.4);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#000000").s().p("AgbBmIAEjqIAzAfIgFDqg");
	this.shape_4.setTransform(5.2,26.5);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("#000000").s().p("AgGA3IACh0IALAIIgCB0g");
	this.shape_5.setTransform(2.8,43);

	this.shape_6 = new cjs.Shape();
	this.shape_6.graphics.f("rgba(255,0,0,0)").s().p("AgyDaIAKnrIBbA4IgKHrg");
	this.shape_6.setTransform(5.2,27.4);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_6},{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,10.4,54.9);


(lib.bubbleBlue = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 2
	this.label = new cjs.Text("", "32px 'Gotham Medium'", "#FFFFFF");
	this.label.name = "label";
	this.label.textAlign = "center";
	this.label.lineHeight = 30;
	this.label.setTransform(38.6,31.8);

	this.timeline.addTween(cjs.Tween.get(this.label).wait(1));

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#0099FF").s().p("ABLFVQglAHgmAAQidAAhxhxQhwhwAAidQAAifBwhwQBxhwCdAAQCfAABvBwQBxBwAACfQAACdhxBwQgmAmgrAaIAAB3g");
	this.shape.setTransform(38.4,41.9);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,76.7,83.8);


(lib.bubble_right = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 2
	this.estimation = new cjs.Text("", "32px 'Gotham Medium'", "#FFFFFF");
	this.estimation.name = "estimation";
	this.estimation.textAlign = "center";
	this.estimation.lineHeight = 30;
	this.estimation.setTransform(38.6,31.8);

	this.timeline.addTween(cjs.Tween.get(this.estimation).wait(1));

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#93AD40").s().p("ABLFVQgkAHgnAAQidAAhxhxQhwhwAAidQAAifBwhwQBxhwCdAAQCfAABvBwQBxBwAACfQAACdhxBwQgmAmgrAaIAAB3g");
	this.shape.setTransform(38.4,41.9,1,1,0,0,180);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,76.7,83.8);


(lib.bubble_left = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 2
	this.estimation = new cjs.Text("", "32px 'Gotham Medium'", "#FFFFFF");
	this.estimation.name = "estimation";
	this.estimation.textAlign = "center";
	this.estimation.lineHeight = 30;
	this.estimation.setTransform(38.6,31.8);

	this.timeline.addTween(cjs.Tween.get(this.estimation).wait(1));

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#93AD40").s().p("ABLFVQgkAHgnAAQidAAhxhxQhwhwAAidQAAifBwhwQBxhwCdAAQCfAABvBwQBxBwAACfQAACdhxBwQgmAmgrAaIAAB3g");
	this.shape.setTransform(38.4,41.9);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,76.7,83.8);


(lib.chariot = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 2
	this.bubble = new lib.bubbleBlue();
	this.bubble.setTransform(14.9,-77.5,0.527,0.498,0,0,32.1);

	this.timeline.addTween(cjs.Tween.get(this.bubble).wait(1));

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#000000").s().p("AkzAaIGVizIDSCBImXCygAkoAaIDFB7IGMiuIjHh7g");
	this.shape.setTransform(30.9,15.5);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#FFFFFF").s().p("AkzAaIGWi0IDRCCImXCyg");
	this.shape_1.setTransform(30.9,15.5);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#000000").s().p("AjLBDIGXiyIAAAtImXCygAjGBGIAAAiIGNitIAAgig");
	this.shape_2.setTransform(41.2,24.3);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#A3A3A3").s().p("AjLBDIGXiyIAAAtImXCyg");
	this.shape_3.setTransform(41.2,24.3);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#000000").s().p("AhmgqIAAgrIDNB+IAAAtgAhhgsIDDB5IAAghIjDh4g");
	this.shape_4.setTransform(10.4,26.8);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("#FFFFFF").s().p("AhmgqIAAgrIDNB+IAAAtg");
	this.shape_5.setTransform(10.4,26.8);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,-77.5,61.7,113.1);


// stage content:
(lib.dictator_simulation = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{init:0,install:3,estimation:73,send:174,transfer:213});

	// timeline functions:
	this.frame_45 = function() {
		/*
		 Process
		 -------
		 Find if canvas in HTML shell page has the following data-attributes:
		 - `data-participants-label-a`
		 - `data-participants-label-b`
		 
		 Use them as attributes in the animation if found.
		 Use default attributes if not.
		 
		 Assumes there is only on canvas in the page.
		 */
		 
		var labelA = 'participant A';
		var labelB = 'participant B';
		
		if (document) {
			var canvas = document.getElementsByTagName('canvas')[0];
			console.log(canvas.dataset);
			if (canvas) {
				labelA = canvas.dataset.participantsLabelA || labelA;
				labelB = canvas.dataset.participantsLabelB || labelB;
			}
		}
		
		this.participantA.label.text = labelA;
		this.participantB.label.text = labelB;
	}
	this.frame_73 = function() {
		/*
		 Process
		 -------
		 Find if canvas in HTML shell page has the following data-attributes:
		 - `data-min`
		 - `data-max`
		 - `data-currency`
		 - `data-locale`
		 
		 Use them as attributes in the animation if found.
		 Use default attributes if not.
		 
		 Assumes there is only on canvas in the page.
		 */
		 
		var self = this;
		var min = 0;
		var max = 12000;
		var currency = '€';
		var locale = 'ko';
		
		if (document) {
			var canvas = document.getElementsByTagName('canvas')[0];
			if (canvas) {
				min = canvas.getAttribute('data-min') || min;
				max = canvas.getAttribute('data-max') || max;
				currency = canvas.getAttribute('data-currency') || currency;
				locale = canvas.getAttribute('data-locale') || locale;
			}
		}
		
		if (locale === 'ko') {
			this.bubbleLeft.estimation.font = "18px 'Gotham Medium'";
			this.bubbleRight.estimation.font = "18px 'Gotham Medium'";
			this.cart.bubble.label.font = "18px 'Gotham Medium'";
		}
		
		this.bubbleLeft.estimation.text = currency + max.toString();
		this.bubbleRight.estimation.text = currency + '0';
		
		this.cart.bubble.alpha = 1;
		this.cart.bubble.label.text = currency + '0';
		
		var givenAmount = 0;
		var unit = locale === 'ko' ? 1000 : 1;
		
		window.DICTATOR = (function () {
			
			var putMoney = function (amount) {
				if (amount >= min && amount <= max) {
					self.bubbleLeft.estimation.text = currency + (max - amount).toString();
					self.cart.bubble.label.text = currency + amount.toString();
					givenAmount = amount;
				}
			};
			
			var send = function () {
				self.gotoAndPlay('send');
				setTimeout(function () {
					self.bubbleRight.estimation.text = currency + givenAmount.toString();
					self.cart.bubble.label.text = currency + '0';
				}, 4500);
			};
			
			return {
				putMoney: putMoney,
				send: send
			};
		})();
	}
	this.frame_78 = function() {
		this.stop();
	}
	this.frame_392 = function() {
		this.gotoAndPlay('estimation');
	}

	// actions tween:
	this.timeline.addTween(cjs.Tween.get(this).wait(45).call(this.frame_45).wait(28).call(this.frame_73).wait(5).call(this.frame_78).wait(314).call(this.frame_392).wait(35));

	// mask (mask)
	var mask = new cjs.Shape();
	mask._off = true;
	var mask_graphics_13 = new cjs.Graphics().p("AKeaLMAAAgi1IO7AAMAAAAi1g");

	this.timeline.addTween(cjs.Tween.get(mask).to({graphics:null,x:0,y:0}).wait(13).to({graphics:mask_graphics_13,x:162.6,y:167.6}).wait(414));

	// portal (front)
	this.instance = new lib.portal("synched",0);
	this.instance.setTransform(290.9,-86.5);
	this.instance._off = true;

	this.instance.mask = mask;

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(13).to({_off:false},0).to({y:233.5},10,cjs.Ease.get(1)).to({_off:true},370).wait(34));

	// bubble right
	this.bubbleRight = new lib.bubble_right();
	this.bubbleRight.setTransform(446.4,222.3,0.096,0.102,0,0,31.3,38.4,38.2);
	this.bubbleRight._off = true;

	this.timeline.addTween(cjs.Tween.get(this.bubbleRight).wait(73).to({_off:false},0).to({regY:38.4,scaleX:1.17,scaleY:1.24,x:488.5,y:227.5},5,cjs.Ease.get(1)).wait(344).to({regY:38.2,scaleX:0.1,scaleY:0.1,x:446.4,y:222.3},4,cjs.Ease.get(1)).wait(1));

	// bubble left
	this.bubbleLeft = new lib.bubble_left();
	this.bubbleLeft.setTransform(136.4,172.3,0.096,0.102,0,0,31.3,38.4,38.2);
	this.bubbleLeft._off = true;

	this.timeline.addTween(cjs.Tween.get(this.bubbleLeft).wait(73).to({_off:false},0).to({regY:38.4,scaleX:1.17,scaleY:1.24,x:117,y:120.4},5,cjs.Ease.get(1)).wait(344).to({regY:38.2,scaleX:0.1,scaleY:0.1,x:136.4,y:172.3},4,cjs.Ease.get(1)).wait(1));

	// participants labels B
	this.participantB = new lib.participant_label();
	this.participantB.setTransform(501.8,339.3,1,1,0,0,0,51.7,30.9);
	this.participantB.alpha = 0;
	this.participantB._off = true;

	this.timeline.addTween(cjs.Tween.get(this.participantB).wait(45).to({_off:false},0).wait(4).to({alpha:1},4,cjs.Ease.get(1)).wait(374));

	// participants labels A
	this.participantA = new lib.participant_label();
	this.participantA.setTransform(173.7,290.8,1,1,0,0,0,51.7,30.9);
	this.participantA.alpha = 0;
	this.participantA._off = true;

	this.timeline.addTween(cjs.Tween.get(this.participantA).wait(45).to({_off:false},0).wait(2).to({alpha:1},4,cjs.Ease.get(1)).wait(376));

	// mask copy (mask)
	var mask_1 = new cjs.Shape();
	mask_1._off = true;
	mask_1.graphics.p("A67fFMAAAg+JMA13AAAMAAAA+Jg");
	mask_1.setTransform(469,213);

	// dols_green copy 11
	this.instance_1 = new lib.dollarsGreen("synched",0);
	this.instance_1.setTransform(124.3,-40.3,1,1,0,0,0,12.1,6.2);
	this.instance_1._off = true;

	this.instance_2 = new lib.dollarsGrey("synched",0);
	this.instance_2.setTransform(186.3,197.2,1,1,0,0,0,12.1,6.2);
	this.instance_2._off = true;

	this.instance_1.mask = this.instance_2.mask = mask_1;

	this.timeline.addTween(cjs.Tween.get(this.instance_1).wait(42).to({_off:false},0).to({y:216.2},3,cjs.Ease.get(1)).wait(138).to({startPosition:0},0).to({y:166.2},7,cjs.Ease.get(1)).wait(11).to({startPosition:0},0).to({x:186.3,y:197.2},8,cjs.Ease.get(1)).to({_off:true},8).wait(210));
	this.timeline.addTween(cjs.Tween.get(this.instance_2).wait(217).to({_off:false},0).to({x:381.1,y:316.6},40,cjs.Ease.get(1)).wait(11).to({startPosition:0},0).to({y:256.6},10,cjs.Ease.get(1)).wait(13).to({startPosition:0},0).to({x:448.1,y:295.2,alpha:0},9,cjs.Ease.get(1)).wait(86).to({startPosition:0},0).to({startPosition:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 12
	this.instance_3 = new lib.dollarsGreen("synched",0);
	this.instance_3.setTransform(124.3,-37.5,1,1,0,0,0,12.1,6.2);
	this.instance_3._off = true;

	this.instance_4 = new lib.dollarsGrey("synched",0);
	this.instance_4.setTransform(186.3,200,1,1,0,0,0,12.1,6.2);
	this.instance_4._off = true;

	this.instance_3.mask = this.instance_4.mask = mask_1;

	this.timeline.addTween(cjs.Tween.get(this.instance_3).wait(41).to({_off:false},0).to({y:219},3,cjs.Ease.get(1)).wait(139).to({startPosition:0},0).wait(1).to({startPosition:0},0).to({y:169},7,cjs.Ease.get(1)).wait(9).to({startPosition:0},0).to({x:186.3,y:200},8,cjs.Ease.get(1)).to({_off:true},9).wait(210));
	this.timeline.addTween(cjs.Tween.get(this.instance_4).wait(217).to({_off:false},0).to({x:381.1,y:319.4},40,cjs.Ease.get(1)).wait(12).to({startPosition:0},0).to({y:259.4},10,cjs.Ease.get(1)).wait(11).to({startPosition:0},0).to({x:448.1,y:298.1},9,cjs.Ease.get(1)).wait(87).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 13
	this.instance_5 = new lib.dollarsGreen("synched",0);
	this.instance_5.setTransform(124.3,-34.6,1,1,0,0,0,12.1,6.2);
	this.instance_5._off = true;

	this.instance_6 = new lib.dollarsGrey("synched",0);
	this.instance_6.setTransform(186.3,202.9,1,1,0,0,0,12.1,6.2);
	this.instance_6._off = true;

	this.instance_5.mask = this.instance_6.mask = mask_1;

	this.timeline.addTween(cjs.Tween.get(this.instance_5).wait(40).to({_off:false},0).to({y:221.9},3,cjs.Ease.get(1)).wait(140).to({startPosition:0},0).wait(2).to({startPosition:0},0).to({y:171.9},7,cjs.Ease.get(1)).wait(7).to({startPosition:0},0).to({x:186.3,y:202.9},8,cjs.Ease.get(1)).to({_off:true},10).wait(210));
	this.timeline.addTween(cjs.Tween.get(this.instance_6).wait(217).to({_off:false},0).to({x:381.1,y:322.3},40,cjs.Ease.get(1)).wait(13).to({startPosition:0},0).to({y:262.3},10,cjs.Ease.get(1)).wait(9).to({startPosition:0},0).to({x:448.1,y:300.9},9,cjs.Ease.get(1)).wait(88).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 14
	this.instance_7 = new lib.dollarsGreen("synched",0);
	this.instance_7.setTransform(124.3,-31.8,1,1,0,0,0,12.1,6.2);
	this.instance_7._off = true;

	this.instance_8 = new lib.dollarsGrey("synched",0);
	this.instance_8.setTransform(186.3,205.7,1,1,0,0,0,12.1,6.2);
	this.instance_8._off = true;

	this.instance_7.mask = this.instance_8.mask = mask_1;

	this.timeline.addTween(cjs.Tween.get(this.instance_7).wait(39).to({_off:false},0).to({y:224.7},3,cjs.Ease.get(1)).wait(141).to({startPosition:0},0).wait(3).to({startPosition:0},0).to({y:174.7},7,cjs.Ease.get(1)).wait(5).to({startPosition:0},0).to({x:186.3,y:205.7},8,cjs.Ease.get(1)).to({_off:true},11).wait(210));
	this.timeline.addTween(cjs.Tween.get(this.instance_8).wait(217).to({_off:false},0).to({x:381.1,y:325.1},40,cjs.Ease.get(1)).wait(14).to({startPosition:0},0).to({y:265.1},10,cjs.Ease.get(1)).wait(7).to({startPosition:0},0).to({x:448.1,y:303.8},9,cjs.Ease.get(1)).wait(89).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 15
	this.instance_9 = new lib.dollarsGreen("synched",0);
	this.instance_9.setTransform(124.3,-28.9,1,1,0,0,0,12.1,6.2);
	this.instance_9._off = true;

	this.instance_10 = new lib.dollarsGrey("synched",0);
	this.instance_10.setTransform(186.3,208.6,1,1,0,0,0,12.1,6.2);
	this.instance_10._off = true;

	this.instance_9.mask = this.instance_10.mask = mask_1;

	this.timeline.addTween(cjs.Tween.get(this.instance_9).wait(38).to({_off:false},0).to({y:227.6},3,cjs.Ease.get(1)).wait(142).to({startPosition:0},0).wait(4).to({startPosition:0},0).to({y:177.6},7,cjs.Ease.get(1)).wait(3).to({startPosition:0},0).to({x:186.3,y:208.6},8,cjs.Ease.get(1)).to({_off:true},12).wait(210));
	this.timeline.addTween(cjs.Tween.get(this.instance_10).wait(217).to({_off:false},0).to({x:381.1,y:328},40,cjs.Ease.get(1)).wait(15).to({startPosition:0},0).to({y:268},10,cjs.Ease.get(1)).wait(5).to({startPosition:0},0).to({x:448.1,y:306.6},9,cjs.Ease.get(1)).wait(90).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 16
	this.instance_11 = new lib.dollarsGreen("synched",0);
	this.instance_11.setTransform(124.3,-26.1,1,1,0,0,0,12.1,6.2);
	this.instance_11._off = true;

	this.instance_11.mask = mask_1;

	this.timeline.addTween(cjs.Tween.get(this.instance_11).wait(37).to({_off:false},0).to({y:230.4},3,cjs.Ease.get(1)).wait(143).to({startPosition:0},0).wait(203).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 17
	this.instance_12 = new lib.dollarsGreen("synched",0);
	this.instance_12.setTransform(124.3,-23.2,1,1,0,0,0,12.1,6.2);
	this.instance_12._off = true;

	this.instance_12.mask = mask_1;

	this.timeline.addTween(cjs.Tween.get(this.instance_12).wait(36).to({_off:false},0).to({y:233.3},3,cjs.Ease.get(1)).wait(144).to({startPosition:0},0).wait(203).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 18
	this.instance_13 = new lib.dollarsGreen("synched",0);
	this.instance_13.setTransform(124.3,-20.4,1,1,0,0,0,12.1,6.2);
	this.instance_13._off = true;

	this.instance_13.mask = mask_1;

	this.timeline.addTween(cjs.Tween.get(this.instance_13).wait(35).to({_off:false},0).to({y:236.1},3,cjs.Ease.get(1)).wait(145).to({startPosition:0},0).wait(203).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 19
	this.instance_14 = new lib.dollarsGreen("synched",0);
	this.instance_14.setTransform(124.3,-17.5,1,1,0,0,0,12.1,6.2);
	this.instance_14._off = true;

	this.instance_14.mask = mask_1;

	this.timeline.addTween(cjs.Tween.get(this.instance_14).wait(34).to({_off:false},0).to({y:239},3,cjs.Ease.get(1)).wait(146).to({startPosition:0},0).wait(203).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 20
	this.instance_15 = new lib.dollarsGreen("synched",0);
	this.instance_15.setTransform(124.3,-14.7,1,1,0,0,0,12.1,6.2);
	this.instance_15._off = true;

	this.instance_15.mask = mask_1;

	this.timeline.addTween(cjs.Tween.get(this.instance_15).wait(33).to({_off:false},0).to({y:241.8},3,cjs.Ease.get(1)).wait(147).to({startPosition:0},0).wait(203).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 21
	this.instance_16 = new lib.dollarsGreen("synched",0);
	this.instance_16.setTransform(124.3,-11.8,1,1,0,0,0,12.1,6.2);
	this.instance_16._off = true;

	this.instance_16.mask = mask_1;

	this.timeline.addTween(cjs.Tween.get(this.instance_16).wait(32).to({_off:false},0).to({y:244.7},3,cjs.Ease.get(1)).wait(148).to({startPosition:0},0).wait(203).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// in_portal
	this.instance_17 = new lib.portal_ray("synched",0);
	this.instance_17.setTransform(293.1,246.2,1,1,0,0,0,31.4,45.6);
	this.instance_17.alpha = 0;
	this.instance_17._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_17).wait(181).to({_off:false},0).to({alpha:1},3).wait(202).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// mask (mask)
	var mask_2 = new cjs.Shape();
	mask_2._off = true;
	var mask_2_graphics_0 = new cjs.Graphics().p("A67fFMAAAg+JMA13AAAMAAAA+Jg");
	var mask_2_graphics_179 = new cjs.Graphics().p("A67fFMAAAg+JMA13AAAMAAAA+Jg");

	this.timeline.addTween(cjs.Tween.get(mask_2).to({graphics:mask_2_graphics_0,x:132.5,y:213}).wait(179).to({graphics:mask_2_graphics_179,x:132.5,y:213}).wait(248));

	// dols_green copy 10
	this.instance_18 = new lib.dollarsGreen("synched",0);
	this.instance_18.setTransform(124.3,-40.3,1,1,0,0,0,12.1,6.2);
	this.instance_18._off = true;

	this.instance_18.mask = mask_2;

	this.timeline.addTween(cjs.Tween.get(this.instance_18).wait(42).to({_off:false},0).to({y:216.2},3,cjs.Ease.get(1)).wait(138).to({startPosition:0},0).to({y:166.2},7,cjs.Ease.get(1)).wait(11).to({startPosition:0},0).to({x:186.3,y:197.2},8,cjs.Ease.get(1)).wait(8).to({startPosition:0},0).to({x:381.1,y:316.6},40,cjs.Ease.get(1)).wait(11).to({startPosition:0},0).to({y:256.6},10,cjs.Ease.get(1)).wait(13).to({startPosition:0},0).to({x:448.1,y:295.2},9,cjs.Ease.get(1)).wait(86).to({startPosition:0},0).to({startPosition:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 9
	this.instance_19 = new lib.dollarsGreen("synched",0);
	this.instance_19.setTransform(124.3,-37.5,1,1,0,0,0,12.1,6.2);
	this.instance_19._off = true;

	this.instance_19.mask = mask_2;

	this.timeline.addTween(cjs.Tween.get(this.instance_19).wait(41).to({_off:false},0).to({y:219},3,cjs.Ease.get(1)).wait(135).to({startPosition:0},0).wait(5).to({startPosition:0},0).to({y:169},7,cjs.Ease.get(1)).wait(9).to({startPosition:0},0).to({x:186.3,y:200},8,cjs.Ease.get(1)).wait(9).to({startPosition:0},0).to({x:381.1,y:319.4},40,cjs.Ease.get(1)).wait(12).to({startPosition:0},0).to({y:259.4},10,cjs.Ease.get(1)).wait(11).to({startPosition:0},0).to({x:448.1,y:298.1},9,cjs.Ease.get(1)).wait(87).to({startPosition:0},0).to({startPosition:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 8
	this.instance_20 = new lib.dollarsGreen("synched",0);
	this.instance_20.setTransform(124.3,-34.6,1,1,0,0,0,12.1,6.2);
	this.instance_20._off = true;

	this.instance_20.mask = mask_2;

	this.timeline.addTween(cjs.Tween.get(this.instance_20).wait(40).to({_off:false},0).to({y:221.9},3,cjs.Ease.get(1)).wait(136).to({startPosition:0},0).wait(6).to({startPosition:0},0).to({y:171.9},7,cjs.Ease.get(1)).wait(7).to({startPosition:0},0).to({x:186.3,y:202.9},8,cjs.Ease.get(1)).wait(10).to({startPosition:0},0).to({x:381.1,y:322.3},40,cjs.Ease.get(1)).wait(13).to({startPosition:0},0).to({y:262.3},10,cjs.Ease.get(1)).wait(9).to({startPosition:0},0).to({x:448.1,y:300.9},9,cjs.Ease.get(1)).wait(88).to({startPosition:0},0).to({startPosition:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 7
	this.instance_21 = new lib.dollarsGreen("synched",0);
	this.instance_21.setTransform(124.3,-31.8,1,1,0,0,0,12.1,6.2);
	this.instance_21._off = true;

	this.instance_21.mask = mask_2;

	this.timeline.addTween(cjs.Tween.get(this.instance_21).wait(39).to({_off:false},0).to({y:224.7},3,cjs.Ease.get(1)).wait(137).to({startPosition:0},0).wait(7).to({startPosition:0},0).to({y:174.7},7,cjs.Ease.get(1)).wait(5).to({startPosition:0},0).to({x:186.3,y:205.7},8,cjs.Ease.get(1)).wait(11).to({startPosition:0},0).to({x:381.1,y:325.1},40,cjs.Ease.get(1)).wait(14).to({startPosition:0},0).to({y:265.1},10,cjs.Ease.get(1)).wait(7).to({startPosition:0},0).to({x:448.1,y:303.8},9,cjs.Ease.get(1)).wait(89).to({startPosition:0},0).to({startPosition:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 6
	this.instance_22 = new lib.dollarsGreen("synched",0);
	this.instance_22.setTransform(124.3,-28.9,1,1,0,0,0,12.1,6.2);
	this.instance_22._off = true;

	this.instance_22.mask = mask_2;

	this.timeline.addTween(cjs.Tween.get(this.instance_22).wait(38).to({_off:false},0).to({y:227.6},3,cjs.Ease.get(1)).wait(138).to({startPosition:0},0).wait(8).to({startPosition:0},0).to({y:177.6},7,cjs.Ease.get(1)).wait(3).to({startPosition:0},0).to({x:186.3,y:208.6},8,cjs.Ease.get(1)).wait(12).to({startPosition:0},0).to({x:381.1,y:328},40,cjs.Ease.get(1)).wait(15).to({startPosition:0},0).to({y:268},10,cjs.Ease.get(1)).wait(5).to({startPosition:0},0).to({x:448.1,y:306.6},9,cjs.Ease.get(1)).wait(90).to({startPosition:0},0).to({startPosition:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 5
	this.instance_23 = new lib.dollarsGreen("synched",0);
	this.instance_23.setTransform(124.3,-26.1,1,1,0,0,0,12.1,6.2);
	this.instance_23._off = true;

	this.instance_23.mask = mask_2;

	this.timeline.addTween(cjs.Tween.get(this.instance_23).wait(37).to({_off:false},0).to({y:230.4},3,cjs.Ease.get(1)).wait(139).to({startPosition:0},0).wait(207).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 4
	this.instance_24 = new lib.dollarsGreen("synched",0);
	this.instance_24.setTransform(124.3,-23.2,1,1,0,0,0,12.1,6.2);
	this.instance_24._off = true;

	this.instance_24.mask = mask_2;

	this.timeline.addTween(cjs.Tween.get(this.instance_24).wait(36).to({_off:false},0).to({y:233.3},3,cjs.Ease.get(1)).wait(140).to({startPosition:0},0).wait(207).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 3
	this.instance_25 = new lib.dollarsGreen("synched",0);
	this.instance_25.setTransform(124.3,-20.4,1,1,0,0,0,12.1,6.2);
	this.instance_25._off = true;

	this.instance_25.mask = mask_2;

	this.timeline.addTween(cjs.Tween.get(this.instance_25).wait(35).to({_off:false},0).to({y:236.1},3,cjs.Ease.get(1)).wait(141).to({startPosition:0},0).wait(207).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy 2
	this.instance_26 = new lib.dollarsGreen("synched",0);
	this.instance_26.setTransform(124.3,-17.5,1,1,0,0,0,12.1,6.2);
	this.instance_26._off = true;

	this.instance_26.mask = mask_2;

	this.timeline.addTween(cjs.Tween.get(this.instance_26).wait(34).to({_off:false},0).to({y:239},3,cjs.Ease.get(1)).wait(142).to({startPosition:0},0).wait(207).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green copy
	this.instance_27 = new lib.dollarsGreen("synched",0);
	this.instance_27.setTransform(124.3,-14.7,1,1,0,0,0,12.1,6.2);
	this.instance_27._off = true;

	this.instance_27.mask = mask_2;

	this.timeline.addTween(cjs.Tween.get(this.instance_27).wait(33).to({_off:false},0).to({y:241.8},3,cjs.Ease.get(1)).wait(143).to({startPosition:0},0).wait(207).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// dols_green
	this.instance_28 = new lib.dollarsGreen("synched",0);
	this.instance_28.setTransform(124.3,-11.8,1,1,0,0,0,12.1,6.2);
	this.instance_28._off = true;

	this.instance_28.mask = mask_2;

	this.timeline.addTween(cjs.Tween.get(this.instance_28).wait(32).to({_off:false},0).to({y:244.7},3,cjs.Ease.get(1)).wait(144).to({startPosition:0},0).wait(207).to({startPosition:0},0).to({alpha:0},6,cjs.Ease.get(1)).to({_off:true},1).wait(34));

	// char_left
	this.instance_29 = new lib.character("synched",0);
	this.instance_29.setTransform(143.4,-48.5,1,1,0,0,0,5.2,27.4);
	this.instance_29._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_29).wait(24).to({_off:false},0).to({y:212},10,cjs.Ease.get(1)).wait(145).to({startPosition:0},0).to({_off:true},214).wait(34));

	// chariot
	this.cart = new lib.chariot();
	this.cart.setTransform(186.2,-35.3,1,1,0,0,0,30.9,17.8);
	this.cart._off = true;

	this.timeline.addTween(cjs.Tween.get(this.cart).wait(20).to({_off:false},0).to({y:210.5},10,cjs.Ease.get(1)).wait(149).to({mode:"synched",startPosition:0},0).wait(38).to({startPosition:0},0).to({x:380.1,y:330.5},40,cjs.Ease.get(1)).wait(129).to({startPosition:0},0).to({alpha:0},6).to({_off:true},1).wait(34));

	// char_right
	this.instance_30 = new lib.character("synched",0);
	this.instance_30.setTransform(421.8,-84.6,1,1,0,0,0,5.2,27.4);
	this.instance_30._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_30).wait(26).to({_off:false},0).to({y:292},9,cjs.Ease.get(1)).wait(144).to({startPosition:0},0).to({_off:true},214).wait(34));

	// portal (back)
	this.instance_31 = new lib.portal("synched",0);
	this.instance_31.setTransform(290.9,-86.5);
	this.instance_31._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_31).wait(13).to({_off:false},0).to({y:233.5},10,cjs.Ease.get(1)).wait(156).to({startPosition:0},0).to({_off:true},214).wait(34));

	// conveyor_belt
	this.instance_32 = new lib.conveyor("synched",0);
	this.instance_32.setTransform(295.3,-126.1);
	this.instance_32._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_32).wait(3).to({_off:false},0).to({y:281.9},10,cjs.Ease.get(1)).wait(166).to({startPosition:0},0).to({_off:true},214).wait(34));

	// floor
	this.instance_33 = new lib.floor("synched",0);
	this.instance_33.setTransform(275,200);

	this.timeline.addTween(cjs.Tween.get(this.instance_33).wait(179).to({startPosition:0},0).to({_off:true},214).wait(34));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(299.9,239.9,600,480);

})(lib = lib||{}, images = images||{}, createjs = createjs||{}, ss = ss||{});
var lib, images, createjs, ss;