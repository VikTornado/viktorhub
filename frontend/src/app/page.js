'use client';

import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { ArrowRight, Code, BookOpen, PenTool } from 'lucide-react';
import Link from 'next/link';
import { useLanguage } from '@/context/LanguageContext';
import { getProjects } from '@/lib/api';

export default function HomePage() {
  const { t, lang } = useLanguage();
  const [featured, setFeatured] = useState([]);

  useEffect(() => {
    getProjects({ is_featured: true }).then((res) => setFeatured(res.data.results)).catch(console.error);
  }, []);

  return (
    <div className="space-y-24">
      {/* Hero Section */}
      <section className="container-custom pt-20 pb-32 flex flex-col items-center text-center">
        <motion.h1 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-5xl md:text-7xl font-bold mb-6 bg-gradient-to-r from-blue-600 to-teal-500 bg-clip-text text-transparent"
        >
          {t.hero.title}
        </motion.h1>
        <motion.p 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-xl md:text-2xl text-gray-600 dark:text-gray-400 mb-10 max-w-2xl"
        >
          {t.hero.subtitle}
        </motion.p>
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
        >
          <Link 
            href="/projects" 
            className="px-8 py-4 bg-blue-600 text-white rounded-full font-semibold hover:bg-blue-700 transition-colors flex items-center gap-2"
          >
            {t.hero.cta}
            <ArrowRight className="w-5 h-5" />
          </Link>
        </motion.div>
      </section>

      {/* Quick Access Grid */}
      <section className="container-custom py-20 bg-gray-50 dark:bg-gray-900 rounded-3xl grid grid-cols-1 md:grid-cols-3 gap-8 p-8">
        <div className="bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-sm hover:shadow-md transition-shadow">
          <Code className="text-blue-600 w-10 h-10 mb-4" />
          <h3 className="text-xl font-bold mb-2">{t.nav.projects}</h3>
          <p className="text-gray-600 dark:text-gray-400 mb-4">Discover the technical solutions and creative projects I've built.</p>
          <Link href="/projects" className="text-blue-600 font-medium flex items-center gap-1">Browse Projects <ArrowRight className="w-4 h-4" /></Link>
        </div>
        <div className="bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-sm hover:shadow-md transition-shadow">
          <BookOpen className="text-teal-600 w-10 h-10 mb-4" />
          <h3 className="text-xl font-bold mb-2">{t.nav.blog}</h3>
          <p className="text-gray-600 dark:text-gray-400 mb-4">Deep dives into technology, tutorials, and industry insights.</p>
          <Link href="/blog" className="text-teal-600 font-medium flex items-center gap-1">Read Blog <ArrowRight className="w-4 h-4" /></Link>
        </div>
        <div className="bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-sm hover:shadow-md transition-shadow">
          <PenTool className="text-purple-600 w-10 h-10 mb-4" />
          <h3 className="text-xl font-bold mb-2">{t.nav.notes}</h3>
          <p className="text-gray-600 dark:text-gray-400 mb-4">Short snippets, quick tips, and coding observations.</p>
          <Link href="/notes" className="text-purple-600 font-medium flex items-center gap-1">Check Notes <ArrowRight className="w-4 h-4" /></Link>
        </div>
      </section>

      {/* Featured Projects Preview */}
      {featured.length > 0 && (
        <section className="container-custom">
          <h2 className="text-3xl font-bold mb-12 flex justify-between items-end">
            {t.projects.title}
            <Link href="/projects" className="text-sm text-blue-600 font-normal hover:underline">{t.projects.all} →</Link>
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {featured.slice(0, 3).map((item) => (
              <motion.div 
                key={item.slug}
                whileHover={{ y: -10 }}
                className="bg-white dark:bg-gray-800 rounded-2xl overflow-hidden border shadow-sm group"
              >
                <div className="h-48 bg-gray-200 dark:bg-gray-700 relative overflow-hidden">
                  {item.cover_image && <img src={item.cover_image} alt="" className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />}
                </div>
                <div className="p-6">
                  <h3 className="text-xl font-bold mb-2">{lang === 'en' ? item.title_en : item.title_uk}</h3>
                  <p className="text-gray-600 dark:text-gray-400 mb-4 line-clamp-2">{lang === 'en' ? item.excerpt_en : item.excerpt_uk}</p>
                  <Link href={`/projects/${item.slug}`} className="text-blue-600 font-semibold inline-flex items-center gap-1 underline underline-offset-4 decoration-2 decoration-blue-200 hover:decoration-blue-600 transition-all">
                    {t.projects.view_details}
                  </Link>
                </div>
              </motion.div>
            ))}
          </div>
        </section>
      )}
    </div>
  );
}
