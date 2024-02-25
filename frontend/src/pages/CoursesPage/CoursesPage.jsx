import React, { useState } from "react"
import style from "./CoursesPage.module.css"
import CourseSearchCard from "../../components/CourseSearchCard/CourseSearchCard"
import { TextField } from "@mui/material"
import { ErrorOutlineRounded } from "@mui/icons-material"

const CoursesPage = (props) => {
    const [coursesList, setCoursesList] = useState(props.coursesList)

    const filterList = (e) => {
        const filteredList = props.coursesList.filter((item) => item.title.toLowerCase().search(e.target.value.toLowerCase()) !== -1)
        setCoursesList(filteredList);
    }

    return (
    <section>
        <div className={style.searchBar}>
            <TextField label="Искать курсы" variant="outlined" type="search" onChange={filterList} sx={{width: "100%"}}/>
        </div>
        <div className={style.coursesWrapper}>
            {coursesList && coursesList.map((item) => <CourseSearchCard setTab={props.setTab} value={item.title} {...item} />)}
            {!coursesList && <div className={style.undefined} ><ErrorOutlineRounded /><h4>По вашему запросу ничего не найдено!</h4></div>}
        </div>
    </section>
    )
}

export default CoursesPage