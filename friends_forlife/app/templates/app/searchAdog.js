document.write('\
					    		<h1>חיפוש כלבים לאימוץ</h1>
						     		<form action="dogs_list" method="get" autocomplete="on" class="adoptDogForm">
										<section class="dog_search_first_section"> 
											<label class="radio_botton_label">
												<h3>מין</h3>
												<input type="radio" name="gender" value="All"><span class="radio_botton">שניהם</span>
												<input type="radio" name="gender" value=״זכר״><span class="radio_botton">זכר</span>
												<input type="radio" name="gender" value="נקבה"><span class="radio_botton">נקבה</span>
											</label>
											<label class="">
												<h3>גודל</h3>
												<select name="dog_size">
													<option value="All">הכול</option>
													<option value="קטן">קטן</option>
													<option value="בינוני">בינוני</option>
													<option value="גדול">גדול</option>
												</select>
											</label>
											<label class="">
												<h3>גיל</h3>
												<select name="dog_age">
													<option value="All">הכול</option>
													<option value="גור">גור</option>
													<option value="צעיר">צעיר</option>
													<option value="בוגר">בוגר</option>
													<option value="מבוגר">מבוגר</option>
												</select>
											</label>
											<label class="">
												<h3>גזע</h3>
												<select name="dog_breed">
													<option value="All">מעורב</option>
													<option value="לברדור">לברדור</option>
													<option value="רועה גרמני">רועה גרמני</option>
													<option value="קבלייר ספניאל">קבלייר ספניאל</option>
													<option value="גולדן רטריבר">גולדן רטריבר</option>
													<option value="בוקסר">בוקסר</option>
													<option value="יורקשיר טרייר">יורקשיר טרייר</option>
													<option value="ביגל">ביגל</option>
													<option value="פודל">פודל</option>
													<option value="שי טסו">שי טסו</option>
													<option value="בול טרייר">בול טרייר</option>
													<option value="בורדר קולי">בורדר קולי</option>
													<option value="פאג">פאג</option>
													<option value="קוקר ספניאל">קוקר ספניאל</option>
													<option value="דלמטי">דלמטי</option>
													<option value="רוטווילר">רוטווילר</option>
													<option value="ג׳ק ראסל">ג'ק ראסל</option>
													<option value="דני ענק">דני ענק</option>
													<option value="דוברמן">דוברמן</option>
													<option value="מלטז">מלטז</option>
													<option value="בולדוג צרפתי">בולדוג צרפתי</option>
													<option value="צ׳יוואווה">צ'יוואווה</option>
													<option value="האסקי סיבירי">האסקי סיבירי</option>
													<option value="פיט בול">פיט בול</option>
												</select>
											</label>
											<label class="">
												<h3>צבעים</h3>
												<select name="dog_color">
													<option value="All">הכול</option>
													<option value="ג׳ינג׳י">ג'ינג'י</option>
													<option value="כהה">כהה</option>
													<option value="צהוב">צהוב</option>
													<option value="שחור">שחור</option>
													<option value="לבן">לבן</option>
												</select>
											</label>
									</section>	
									<section class="dog_search_second_section">	
										<h3>תכונות אופי</h3>
										<input type="checkbox" name="Characteristics[]" value="childrens_friendly"><label>ידידותי לילדים</label><br>
										<input type="checkbox" name="Characteristics[]" value="suitable_for_allergic"><label>מתאים לאלרגיים</label><br>
	                                    <input type="checkbox" name="Characteristics[]" value="habituated_for_needs"><label>מחונך לצרכים</label>
	                                    <input type="submit">
	                                </section>
									<div class="clear"></div>
								</form>