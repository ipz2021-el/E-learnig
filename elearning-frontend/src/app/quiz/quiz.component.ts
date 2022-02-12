import { Component, OnInit } from '@angular/core';
import { Model, SurveyNG } from "survey-angular";
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute } from "@angular/router";
import { Router } from '@angular/router';

@Component({
  selector: 'app-quiz',
  templateUrl: './quiz.component.html',
  styleUrls: ['./quiz.component.scss']
})
export class QuizComponent implements OnInit {

  survey_css = {
    navigationButton: "cds-button"
  }

  quiz:any;

  surveyJson = {
    showProgressBar: "top",
    showTimerPanel: "top",
    maxTimeToFinishPage: 10,
    maxTimeToFinish: 30,
    firstPageIsStarted: true,
    startSurveyText: "Rozpocznij test!",
    pages: [],
    completedHtml: "<h4>Udzielono <b>{correctedAnswers}</b> poprawnych odpowiedzi na <b>{questionCount}</b> możliwych.</h4>"
  };

  constructor(private http: HttpClient, private route: ActivatedRoute, private router: Router) { }

  ngOnInit(): void {
    this.router.routeReuseStrategy.shouldReuseRoute = () => {
      // do your task for before route
      return false;
    }

    this.quizzes_endpoint().subscribe((res) => {
      let quizzes:any = res;
      this.quiz = quizzes.filter((c: any) => c.id == this.route.snapshot.paramMap.get("id"))[0]
      this.surveyJson.pages = this.quiz.pages;
      const survey = new Model(this.surveyJson);
      SurveyNG.render("surveyContainer", { model: survey, css: this.survey_css});
    })
  }

  quizzes_endpoint() {
    return this.http.get('http://localhost:3000/quizzes');
  }

}
