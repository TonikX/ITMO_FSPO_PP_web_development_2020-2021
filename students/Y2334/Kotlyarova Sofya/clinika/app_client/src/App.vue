<template>
    <v-app>
        <v-app-bar app>
            <v-app-bar-title>
                Clinika
            </v-app-bar-title>
        </v-app-bar>

        <v-main>
            <v-container>
                <v-row>
                    <v-col
                        cols="3"
                    >
                        <v-card
                            class="mx-auto"
                            max-width="400"
                            tile
                        >
                            <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title>
                                        <router-link to="clients">
                                            Clients
                                        </router-link>
                                    </v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>

                            <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title>
                                        <router-link to="services">
                                            Services
                                        </router-link>
                                    </v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>

                            <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title>
                                        <router-link to="doctors">
                                            Doctors
                                        </router-link>
                                    </v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>

                            <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title>
                                        <router-link to="doctor-services">
                                            Doctor Services
                                        </router-link>
                                    </v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>

                            <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title>
                                        <router-link to="tickets">
                                            Tickets
                                        </router-link>
                                    </v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                        </v-card>
                    </v-col>
                    <v-col
                        cols="9"
                    >
                        <router-view></router-view>
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>
