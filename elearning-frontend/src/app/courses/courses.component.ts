import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-courses',
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.scss']
})
export class CoursesComponent implements OnInit {

  constructor() { }

  searchword = ''

  search(e: any) {
    console.log(this.searchword);
    this.courses_displayed = this.courses.filter(c => c.title.toLowerCase().includes(this.searchword))
  }

  courses_displayed: any;
  courses = [
    {
      image: 'jupiter-planet',
      title: 'Fizyka i astronomia',
      tutor: 'Milena Michalska',
    },
    {
      image: 'story-book',
      title: 'Czary i magia',
      tutor: 'Paweł Gaborek',
    },
    {
      image: 'calculator',
      title: 'Analiza matematyczna',
      tutor: 'Maciej Lewicki',
    },
    {
      image: 'alcohol-burner',
      title: 'Chemia eksperymentalna',
      tutor: 'Paweł Gaborek',
    },
    {
      image: 'planetarium',
      title: 'Wstęp do obserwacji nieba',
      tutor: 'Jan Kowalski',
    },
    {
      image: 'student',
      title: 'Seminarium dyplomowe',
      tutor: 'Jan Kowalski',
    },
    {
      image: 'biotech',
      title: 'Podstawy genetyki',
      tutor: 'Jan Kowalski',
    },
    {
      image: 'brain',
      title: 'Sztuczna inteligencja',
      tutor: 'Jan Kowalski',
    }
  ]

  ngOnInit(): void {
    this.courses_displayed = this.courses;
  }

}
