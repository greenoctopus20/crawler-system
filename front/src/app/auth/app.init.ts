import { KeycloakService } from 'keycloak-angular';

export function initializeKeycloak(keycloak: KeycloakService): () => Promise<boolean> {
    return () =>
        keycloak.init({
            config: {
                url: 'http://localhost:8085/',
                realm: 'angular',
                clientId: 'angular-client-one',
            },
            initOptions: {
                checkLoginIframe: false,
            },
            loadUserProfileAtStartUp: true,
            //enableBearerInterceptor: true, // Add this line to enable the Bearer interceptor
        });

    }