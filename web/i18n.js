const I18n = {
    language: 'pt-BR',
    setLanguage() {
        this.language = 'pt-BR';
        document.documentElement.lang = 'pt-BR';
        document.documentElement.dir = 'ltr';
    },
    t(key) {
        return key;
    },
    x(key) {
        return key;
    }
};
