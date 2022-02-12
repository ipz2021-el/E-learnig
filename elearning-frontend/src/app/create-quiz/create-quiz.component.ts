import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-create-quiz',
  templateUrl: './create-quiz.component.html',
  styleUrls: ['./create-quiz.component.scss']
})
export class CreateQuizComponent implements OnInit {

  constructor(private http: HttpClient, private router: Router) { }

  title = '';
  image = '';
  course = '';
  pages: any[] = [{ questions: [] }]
  q1 = '';
  q1r = '';
  q1a1 = '';
  q1a2 = '';
  q1a3 = '';

  q2 = '';
  q2r = '';
  q2a1 = '';
  q2a2 = '';
  q2a3 = '';

  q3 = '';
  q3r = '';
  q3a1 = '';
  q3a2 = '';
  q3a3 = '';

  quizzes_endpoint(body:any) {
    return this.http.post('http://localhost:3000/quizzes', body);
  }

  icons = ['curriculum', 'alcohol-burner', 'biotech', 'brain', 'calculator', 'computer', 'jupiter-planet', 'mobile', 'planetarium', 'story-book', 'student']

  ngOnInit(): void {}

  send() {

   this.pages.push(
    {
      questions: [
        {
          type: "radiogroup",
        name: "q1",
        title: this.q1,
        choices: [this.q1a1, this.q1a2, this.q1a3],
        correctAnswer: this.q1r
        }
      ]
    }
   )

   this.pages.push(
    {
      questions: [
        {
          type: "radiogroup",
        name: "q2",
        title: this.q2,
        choices: [this.q2a1, this.q2a2, this.q2a3],
        correctAnswer: this.q2r
        }
      ]
    }
   )

   this.pages.push(
    {
      questions: [
        {
          type: "radiogroup",
        name: "q3",
        title: this.q3,
        choices: [this.q3a1, this.q3a2, this.q3a3],
        correctAnswer: this.q3r
        }
      ]
    }
   )

    let body = 
    {
      id: Date.now(),
      image: this.image,
      title: this.title,
      pages: this.pages,
      joined: false
    }

    this.quizzes_endpoint(body).subscribe((res) => {
      console.log(res);
      this.router.navigate(['/quizzes']);
    })
  }
}
