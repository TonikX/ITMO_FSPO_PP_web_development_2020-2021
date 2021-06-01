<template>
    <div>
        <LecturersList msg="Список преподавателей"/>
    </div>
</template>

<script>
import LecturersList from "../components/lecturers/LecturersList";

export default {
    name: 'Lecturers',
    components: {
        LecturersList
    }
}
</script>