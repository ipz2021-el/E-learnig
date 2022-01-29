import { Component, OnInit } from '@angular/core';
import { Model, SurveyNG } from "survey-angular";

@Component({
  selector: 'app-quiz',
  templateUrl: './quiz.component.html',
  styleUrls: ['./quiz.component.scss']
})
export class QuizComponent implements OnInit {

  survey_css = {
    navigationButton: "cds-button"
  }

  surveyJson = {
    showProgressBar: "top",
    showTimerPanel: "top",
    maxTimeToFinishPage: 10,
    maxTimeToFinish: 30,
    firstPageIsStarted: true,
    startSurveyText: "Rozpocznij test!",
    pages: [
        {
            questions: []
        }, {
            questions: [
                {
                    type: "radiogroup",
                    name: "srs",
                    title: "Rozwiń skrót SRS?",
                    choices: [
                        "Software Requirements Specification", "System Requirements Spreadsheet", "Software Random Systems"
                    ],
                    correctAnswer: "Software Requirements Specification"
                }
            ]
          }, {
            questions: [
                {
                    type: "radiogroup",
                    name: "srs1",
                    title: "Rozwiń skrót SRS?",
                    choices: [
                        "Software Requirements Specification", "System Requirements Spreadsheet", "Software Random Systems"
                    ],
                    correctAnswer: "Software Requirements Specification"
                }
            ]
          }, {
            questions: [
                {
                    type: "radiogroup",
                    name: "srs2",
                    title: "Rozwiń skrót SRS?",
                    choices: [
                        "Software Requirements Specification", "System Requirements Spreadsheet", "Software Random Systems"
                    ],
                    correctAnswer: "Software Requirements Specification"
                }
            ]
        }
    ],
    completedHtml: "<h4>Udzielono <b>{correctedAnswers}</b> poprawnych odpowiedzi na <b>{questionCount}</b> możliwych.</h4>"
  };

  constructor() { }

  ngOnInit(): void {
    const survey = new Model(this.surveyJson);
    SurveyNG.render("surveyContainer", { model: survey, css: this.survey_css});
  }

}
