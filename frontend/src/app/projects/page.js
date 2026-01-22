'use client';

import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { getProjects } from '@/lib/api';
import { useLanguage } from '@/context/LanguageContext';
import Link from 'next/link';

export default function ProjectsPage() {
  const { t, lang } = useLanguage();
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    getProjects().then(res => setProjects(res.data.results)).catch(console.error);
  }, []);

  return (
    <div className="container-custom py-20">
      <h1 className="text-4xl font-bold mb-12">{t.projects.title}</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {projects.map((item, index) => (
          <motion.div 
            key={item.slug}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1 }}
            className="bg-white dark:bg-gray-800 rounded-2xl overflow-hidden border shadow-sm group hover:shadow-lg transition-all"
          >
            <div className="h-48 bg-gray-200 dark:bg-gray-700 relative">
              {item.cover_image && <img src={item.cover_image} alt="" className="w-full h-full object-cover" />}
            </div>
            <div className="p-6">
              <div className="flex flex-wrap gap-2 mb-3">
                {item.tags.map(tag => (
                  <span key={tag.slug} className="text-[10px] uppercase tracking-wider font-bold px-2 py-1 bg-blue-100 text-blue-600 rounded">
                    {tag.name}
                  </span>
                ))}
              </div>
              <h3 className="text-xl font-bold mb-2 group-hover:text-blue-600 transition-colors uppercase">
                {lang === 'en' ? item.title_en : item.title_uk}
              </h3>
              <p className="text-gray-600 dark:text-gray-400 mb-6 line-clamp-2">
                {lang === 'en' ? item.excerpt_en : item.excerpt_uk}
              </p>
              <Link href={`/projects/${item.slug}`} className="w-full inline-block text-center py-2 border-2 border-blue-600 text-blue-600 rounded-lg font-semibold hover:bg-blue-600 hover:text-white transition-all">
                {t.projects.view_details}
              </Link>
            </div>
          </motion.div>
        ))}
      </div>
    </div>
  );
}
