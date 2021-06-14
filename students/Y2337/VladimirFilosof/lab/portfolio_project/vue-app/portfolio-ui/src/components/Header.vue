<template>
	<header class="header bg-gray">
		<div class="container">
			<nav class="navbar navbar-expand-md navbar-light">
				<a class="navbar-brand logo" href="#">IT Filosof</a>
				<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
					aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
					<span class="navbar-toggler-icon"></span>
				</button>
				<div class="collapse navbar-collapse justify-content-end" id="navbarNav">
					<ul class="navbar-nav text-center">
						<li class="nav-item">
							<a class="nav-link active" aria-current="page" href="/">Главная</a>
						</li>
						<li class="nav-item">
							<a class="nav-link" href="/projects/">Работы</a>
						</li>
						<li  class="nav-item">
							<a class="nav-link" href="/services/">Услуги</a>
						</li>
						<li class="nav-item">
							<a class="nav-link" href="/lichniy-kabinet/">Личный кабинет</a>
						</li>
					</ul>
				</div>
			</nav>
		</div>
	</header>
</template>

<script>
export default {
	name: 'Header'
}

</script>

<style lang="sass">
.bg-gray
	background-color: #E5E5E5
</style>
