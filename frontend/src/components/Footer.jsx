import { siteConfig } from '@/lib/config';
import { Github, Linkedin, Send, Instagram, Twitter, Youtube } from 'lucide-react';
import { useLanguage } from '@/context/LanguageContext';

const socialIcons = {
  github: Github,
  linkedin: Linkedin,
  telegram: Send,
  instagram: Instagram,
  twitter: Twitter,
  youtube: Youtube,
};

export default function Footer() {
  const { t } = useLanguage();
  
  return (
    <footer className="bg-gray-50 dark:bg-gray-900 border-t mt-20">
      <div className="container-custom py-12">
        <div className="flex flex-col md:flex-row justify-between items-center gap-8">
          <div>
            <h2 className="text-2xl font-bold mb-2">{siteConfig.name}</h2>
            <p className="text-gray-600 dark:text-gray-400 max-w-xs transition-colors">
              Building meaningful digital experiences with precision and passion.
            </p>
          </div>
          
          <div className="flex flex-col items-center md:items-end gap-4">
            <div className="flex gap-4">
              {Object.entries(siteConfig.links).map(([name, url]) => {
                const Icon = socialIcons[name];
                return (
                  <a 
                    key={name}
                    href={url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="p-2 bg-white dark:bg-gray-800 rounded-full border hover:text-blue-600 hover:border-blue-600 transition-all transition-colors"
                    aria-label={name}
                  >
                    <Icon className="w-5 h-5" />
                  </a>
                );
              })}
            </div>
            <p className="text-sm text-gray-500">
              © {new Date().getFullYear()} {siteConfig.name}. {t.footer.rights}
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
}
