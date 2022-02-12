import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-quizzes',
  templateUrl: './quizzes.component.html',
  styleUrls: ['./quizzes.component.scss']
})
export class QuizzesComponent implements OnInit {

  constructor(private http: HttpClient) { }

  quizzes:any;

  courses_endpoint() {
    return this.http.get('http://localhost:3000/quizzes');
  }

  ngOnInit(): void {
    this.courses_endpoint().subscribe((res) => {
      this.quizzes = res
    })
  }

}
