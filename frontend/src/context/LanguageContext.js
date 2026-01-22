'use client';

import React, { createContext, useContext, useState, useEffect } from 'react';
import en from '../locales/en.json';
import uk from '../locales/uk.json';

const LanguageContext = createContext();

export function LanguageProvider({ children }) {
  const [lang, setLang] = useState('en');
  const [translations, setTranslations] = useState(en);

  useEffect(() => {
    const savedLang = localStorage.getItem('lang') || 'en';
    setLang(savedLang);
    setTranslations(savedLang === 'en' ? en : uk);
  }, []);

  const toggleLang = () => {
    const newLang = lang === 'en' ? 'uk' : 'en';
    setLang(newLang);
    setTranslations(newLang === 'en' ? en : uk);
    localStorage.setItem('lang', newLang);
  };

  return (
    <LanguageContext.Provider value={{ lang, t: translations, toggleLang }}>
      {children}
    </LanguageContext.Provider>
  );
}

export const useLanguage = () => useContext(LanguageContext);
