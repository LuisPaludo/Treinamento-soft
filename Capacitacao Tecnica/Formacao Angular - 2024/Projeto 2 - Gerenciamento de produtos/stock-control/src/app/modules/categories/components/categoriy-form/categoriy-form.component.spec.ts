import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CategoriyFormComponent } from './categoriy-form.component';

describe('CategoriyFormComponent', () => {
  let component: CategoriyFormComponent;
  let fixture: ComponentFixture<CategoriyFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CategoriyFormComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CategoriyFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
